# https://asyncssh.readthedocs.io/en/latest/#server-examples
import asyncio, asyncssh, bcrypt, os, sys, shlex, pathlib
from typing import Optional

import shared

passwords = {
    shared.NAME.lower(): shared.PASSWORD,
}

async def handle_client(process: asyncssh.SSHServerProcess) -> None:
    username: str = process.get_extra_info('username')
    current_directory: pathlib.Path = pathlib.Path("/")

    process.stdout.write(f"\x1b[0m=== \x1b[1m{shared.NAME.upper()}'S \x1b[31mF\x1b[33mU\x1b[32mN \x1b[36mZ\x1b[34mO\x1b[35mN\x1b[31mE\x1b[37m!!!\x1b[0m ===\r\n")
    process.stdout.write("This is my custom shell, there's not much in it right now, but remember how to navigate a terminal and you'll be fine! :>\r\n")

    # This should prevent escapes
    def resolve_paths(virtual: pathlib.Path = pathlib.Path(".")) -> tuple[pathlib.Path, pathlib.Path]:
        path: pathlib.Path = (current_directory / pathlib.Path(virtual)).resolve()
        rel: str = str(path)[1:]
        real: pathlib.Path = pathlib.Path(shared.FOLDER) / rel
        return path, real
    # Makes printing to the shell easier
    def prompt() -> None:
        process.stdout.write("\r\n\x1b[34m" + str(current_directory) + " \x1b[36m$\x1b[0m ")
    def error(message: str) -> None:
        process.stdout.write(f"\x1b[31mError:\x1b[0m {message} \x1b[31m:(\x1b[0m\r\n")
    def println(text: str) -> None:
        process.stdout.write(text + "\r\n")

    prompt()
    async for line in process.stdin:
        args = shlex.split(line.strip(), comments=True)
        if len(args) > 0:
            if args[0] == "ls":
                virtual, real = resolve_paths(pathlib.Path(args[1]) if len(args) > 1 else pathlib.Path("."))
                if real.is_dir():
                    for file in os.listdir(real):
                        println(file)
                elif real.exists():
                    println(str(real))
                else:
                    error("File doesn't exist")
            elif args[0] == "cd":
                if len(args) < 2:
                    error("Requires a \x1b[32mpath\x1b[0m")
                else:
                    virtual, real = resolve_paths(args[1])
                    if real.is_dir():
                        current_directory = virtual
                    elif real.exists():
                        error("That's not a folder!")
                    else:
                        error("That folder doesn't exist!")
            elif args[0] == "cat":
                if len(args) < 2:
                    error("Requires a \x1b[32mpath\x1b[0m")
                else:
                    virtual, real = resolve_paths(args[1])
                    if real.is_dir():
                        error("That's a folder!")
                    elif real.exists():
                        try:
                            with real.open("r") as f:
                                println(f.read())
                        except Exception as e:
                            print(f"Error in '{line.strip()}': " + str(e))
                            error("Can't print this file")
                    else:
                        error("That file doesn't exist!")
            elif args[0] == "echo":
                println(line.strip()[5:])
            elif args[0] == "exit":
                process.exit(0)
            elif args[0] == "help":
                println("Use \x1b[36mecho\x1b[0m, \x1b[36mls\x1b[0m, \x1b[36mcd\x1b[0m, \x1b[36mcat\x1b[0m, and \x1b[36mexit\x1b[0m!")
            else:
                error("Unknown command")
        prompt()
        await process.stdout.drain()
    process.exit(0)

class MySSHServer(asyncssh.SSHServer):
    def connection_made(self, conn: asyncssh.SSHServerConnection) -> None:
        peername = conn.get_extra_info('peername')[0]
        print(f'SSH connection received from {peername}.')

    def connection_lost(self, exc: Optional[Exception]) -> None:
        if exc:
            print('SSH connection error: ' + str(exc), file=sys.stderr)
        else:
            print('SSH connection closed.')

    def begin_auth(self, username: str) -> bool:
        # If the user's password is the empty string, no auth is required
        return passwords.get(username.lower()) != b''

    def password_auth_supported(self) -> bool:
        return True

    def validate_password(self, username: str, password: str) -> bool:
        username = username.lower()
        if username not in passwords:
            return False
        pw = passwords[username]
        if not password and not pw:
            return True
        return bcrypt.checkpw(password.encode('utf-8'), pw)

# Call this from gate
async def start_server() -> None:
    while True:
        try:
            server: asyncssh.SSHAcceptor
            server = await asyncssh.create_server(MySSHServer, '127.0.0.1', shared.SSH_PORT,
                                           server_host_keys=['ssh_server'],
                                           process_factory=handle_client)

            await server.wait_closed()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("SSH:", e)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(start_server())
    except (OSError, asyncssh.Error) as exc:
        sys.exit('Error starting server: ' + str(exc))

    loop.run_forever()
