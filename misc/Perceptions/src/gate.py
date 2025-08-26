import asyncio
import enum

import shared

# Only SSH and HTTP are used in the challenge but other
# protocols can still be recognised

class Protocol(enum.Enum):
    UNKNOWN = -1
    MQTT = 0
    HTTP = 1
    REDIS = 2
    SSH = 3

def matches(lyst: list[bytes], item: bytes) -> bool:
    item_len: int = len(item)
    for potential in lyst:
        smallest = min(len(potential), item_len)
        if potential[:smallest] == item[:smallest]:
            return True
    return False
def matches_one(potential: bytes, item: bytes) -> bool:
    smallest = min(len(potential), len(item))
    if potential[:smallest] == item[:smallest]:
        return True
    return False

# Methods are case sensitive
# Methods from https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods
HTTP_SIGNATURES: list[int] = [
    b"GET ",
    b"HEAD ",
    b"POST ",
    b"DELETE ",
    b"CONNECT ",
    b"OPTIONS ",
    b"TRACE ",
    b"PATCH ",
    b"PUT "
]
# https://redis.io/docs/latest/develop/reference/protocol-spec/
# Commands usually encoded with '*1\r\n$5\r\nHELLO', etc., but don't have to be
# REDIS should also be fallback as it has numerous commands
REDIS_BYTES: list[int] = [
    ord("+"),
    ord("-"),
    ord(":"),
    ord("$"),
    ord("*"),
    ord("_"),
    ord("#"),
    ord(","),
    ord("("),
    ord("!"),
    ord("="),
    ord("%"),
    ord("`"),
    ord("~"),
    ord(">"),
]

CONNECTIONS: dict[Protocol, tuple] = {
    Protocol.HTTP: ("127.0.0.1", shared.HTTP_PORT),
    #Protocol.MQTT: ("127.0.0.1", shared.MQTT_PORT),
    #Protocol.REDIS: ("127.0.0.1", shared.REDIS_PORT),
    Protocol.SSH: ("127.0.0.1", shared.SSH_PORT),
}

async def proxy(reader, writer):
    protocol: Protocol = Protocol.UNKNOWN
    already_taken: bytes = b""
    data = await reader.read(16)
    already_taken += data
    if data[0] == 16:
        protocol = Protocol.MQTT
    elif matches_one(b"GET ", data):
        if data[4] == ord("/"):
            protocol = Protocol.HTTP
        else:
            protocol = Protocol.MQTT
    elif matches(HTTP_SIGNATURES, data):
        protocol = Protocol.HTTP
    elif matches_one(b"SSH-2.", data):
        protocol = Protocol.SSH
    # Remove REDIS fallback to prevent confusing people
    #else:
    #    protocol = Protocol.REDIS

    async def forward(reader, writer):
        while not writer.is_closing():
            data: bytes = await reader.read(1024)
            if not data:
                break
            writer.write(data)
            await writer.drain()

    # Create the proxied connection
    if protocol not in CONNECTIONS:
        # Unsupported
        supported: bytes = b", ".join(proto.name.encode() for proto in CONNECTIONS)
        writer.write(b"Detected protocol '" + protocol.name.encode() + b"', Perceptions cannot serve this protocol. Supported: " + supported + b"\r\n")
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        return
    try:
        proxied_reader, proxied_writer = await asyncio.open_connection(*CONNECTIONS[protocol])
    except ConnectionRefusedError:
        print(f"Could not create connection to {CONNECTIONS[protocol]}, connection refused.")
        writer.close()
        await writer.wait_closed()
        return
    # Write everything we collected that we now need to pass on
    proxied_writer.write(already_taken)
    await writer.drain()
    tasks = [
        asyncio.create_task(forward(proxied_reader, writer)),
        asyncio.create_task(forward(reader, proxied_writer)),
    ]
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    writer.close()
    proxied_writer.close()
    await writer.wait_closed()
    await proxied_writer.wait_closed()

async def start_gate_server():
    server = await asyncio.start_server(
        proxy, '', shared.GATE_PORT)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

async def main():
    import ssh, web

    ssh_server = asyncio.create_task(ssh.start_server())
    http_server = asyncio.create_task(web.start_server())
    gate_server = asyncio.create_task(start_gate_server())

    tasks = [ssh_server, http_server, gate_server]

    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in tasks:
        task.cancel()

asyncio.run(main())
