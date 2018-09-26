"""
A simple example of asyncio with Python3.7

Expected return of the script

Wed Sep 26 12:44:16 2018 Hello!
Wed Sep 26 12:44:16 2018 Hello from a thread!
Wed Sep 26 12:44:17 2018 Goodbye!

"""

import time
import asyncio


async def main_block():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


async def blocking():
    await asyncio.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")


async def main():
    task = asyncio.create_task(blocking())
    await main_block()
    task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
