import asyncio
from watchfiles import awatch

async def main():
    stop_event = asyncio.Event()

    async def stop_soon():
        await asyncio.sleep(3)
        stop_event.set()

    stop_soon_task = asyncio.create_task(stop_soon())

    async for changes in awatch("test.py", stop_event=stop_event):
        print(changes)

    await stop_soon_task

asyncio.run(main())
