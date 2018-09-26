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


def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")


async def main():
    loop = asyncio.get_running_loop()
    # The function run_in_executor runs a blocking function asynchronously and
    # returns a Future
    loop.run_in_executor(None, blocking)
    await main_block()


if __name__ == "__main__":
    asyncio.run(main())
