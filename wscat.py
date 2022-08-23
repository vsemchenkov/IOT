import websockets
import asyncio
import sys

uri = sys.argv[1]

async def ws(error):
    async with websockets.connect(uri=uri) as websocket:
        while True:
            print('Starting...' + str(error))
            try:
                message = await websocket.recv()
                print(message)
                if error:
                    raise ValueError('Exception')
            except Exception as e:
                print(e)
            print('Finishing...' + str(error))
            await asyncio.sleep(1)


async def main():
    # try:
    ws_task_error = loop.create_task(ws(error=True))
    # ws_task_fine = loop.create_task(ws(False))
    await asyncio.wait([ws_task_error])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()