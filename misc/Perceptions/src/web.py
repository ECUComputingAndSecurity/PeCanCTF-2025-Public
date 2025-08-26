from quart import Quart, render_template, redirect
import asyncio

import shared

app = Quart(__name__, static_url_path='', static_folder=shared.FOLDER)

@app.route("/name")
async def name():
    return shared.NAME

# Just makes it easier for players
@app.route("/")
async def index():
    return redirect("/25YDY4737K3QMIZ6N5OUEYGL/page.html", code=308)

async def start_server():
    while True:
        try:
            await app.run_task(host="127.0.0.1", port=shared.HTTP_PORT)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("HTTP:", e)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(start_server())
    except Exception as exc:
        sys.exit('Error starting server: ' + str(exc))

    loop.run_forever()
