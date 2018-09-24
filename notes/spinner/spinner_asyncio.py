"""
With python3.7
"""

import asyncio
import itertools
import sys
import time


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg
        write(status)
        flush()
        # move the cursor back with the backspace character \x08
        write('\x08' * len(status))
        # asyncio.sleep sleeps without blocking the event loop
        await asyncio.sleep(.1)
    write(' ' * len(status) + '\x08' * len(status))


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    print(time.strftime("[%H:%M:%S]"), "supervisor starts...")
    # When you create a task object, it is already scheduled to run
    spin_task = asyncio.create_task(spin("Thinking"))
    print(spin_task)
    result = await slow_function()
    spin_task.cancel()
    print(time.strftime("[%H:%M:%S]"), "supervisor done.")
    return result


async def main():
    result = await supervisor()
    print("Answer:", result)


if __name__ == "__main__":
    asyncio.run(main())
