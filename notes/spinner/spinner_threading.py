import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    """
    This function will run in separate thread
    """
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle("|/-\\"):
        status = char + " " + msg
        write(status)
        flush()
        # move the cursor back with the backspace character \x08
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    # Pretend a long waiting time
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=["Thinking", signal])
    print("spinner object:", spinner)
    spinner.start()
    # The running of slow_function blocks the main thread while the spinner
    # continues to run on the secondary thread
    result = slow_function()
    signal.go = False
    # Wait till the spinner thread finishes
    spinner.join()
    return result


def main():
    result = supervisor()
    print("Answer:", result)


if __name__ == "__main__":
    main()
