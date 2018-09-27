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
    print(time.strftime("[%H:%M:%S]"), "entering slow_function...")
    await asyncio.sleep(3)
    return 42


async def supervisor():
    """
    The execution order of this function is exactly as a Python coroutine.

    The Python async runs with one main thread in general. So the main thread
    first executes till the line `await asyncio.sleep(.1)` of the function spin,
    then instead of waiting inside the function spin, the control is
    yielded back to the main thread and the execution continues to print the
    spin_task and then to `await` the slow function. The await is composed of
    two steps: wrap the coroutine into a Task and yield the result. Once the
    line await in slow_function is hit, the control is again handed back to
    the main thread.

    We noticed that the spin_task and slow_function are two tasks managed by
    the event loop. The event loop alternate the execution between the two
    tasks.

    """
    print(time.strftime("[%H:%M:%S]"), "supervisor starts...")
    # When you create a task object, it is already scheduled to run
    spin_task = asyncio.create_task(spin("Thinking"))
    print(spin_task)
    # The event loop continues to run after we called the slow_function as it
    # hands the control back with await asyncio.sleep
    result = await slow_function()
    spin_task.cancel()
    print(time.strftime("[%H:%M:%S]"), "supervisor done.")
    return result


async def main():
    result = await supervisor()
    print("Answer:", result)


if __name__ == "__main__":
    asyncio.run(main())
