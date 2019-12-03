import asyncio
import websockets
import time

async def hello():
    uri = "ws://192.168.0.107:9001"
    async with websockets.connect(uri) as websocket:
        for x in range(10):
            time.sleep(1)
            await websocket.send("MT;5;868446031850114;R0;5+191202100809+42.20725+-85.62916+0.00+342+2+3976+208")
            #await websocket.recv()
            print("sending packet %s",x)

asyncio.get_event_loop().run_until_complete(hello())