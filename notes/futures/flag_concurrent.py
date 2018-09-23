"""
The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

- ThreadPoolExecutor is an Executor subclass that uses a pool of threads
to execute calls asynchronously. Python threads are well suited for I/O
intensive applications.
- The ProcessPoolExecutor class is an Executor subclass that uses a pool of
processes to execute calls asynchronously. (for CPU-bound processing)

## Future

Futures encapsulate pending operations so that they can be put in queues.
Their state of completion can be queried and their result can be retrieved
when available.

The Executor.submit method schedules a callable fn to be executed, it returns
a **Future** representing the scheduling of the execution.

The state of the future is only changed by the concurrency framework, not by
the client code.


## concurrent.futures

The following examples are limited by GIL(Global Interpreter Lock) that only
lets one thread run at any time.

When we write Python code we have no control over GIL, but a built-in function
or an extension in C can release the GIL while running time consuming tasks.

However, all standard library functions that perform blocking I/O release the
GIL when waiting for a result from OS.

Run the script with

$ python -m futures.flag_sequential


References
----------
https://docs.python.org/3/library/concurrent.futures.html

"""
from concurrent import futures

from .flag_sequential import main, download_flag

MAX_WORKERS = 20


def download_flags_with_map(executor):
    """
     The exc.__exit__ calls the exc.shutdown(wait=True), which will block till
    all threads/processes are done.
    """
    def download_flags(countries):
        with executor(MAX_WORKERS) as exc:
            return len(list(exc.map(download_flag, countries)))
    return download_flags


def download_flags_with_future(countries):
    print("--> with futures")
    with futures.ThreadPoolExecutor(MAX_WORKERS) as exc:
        futures_ = [exc.submit(download_flag, c) for c in countries]
        # The function as_completed yields futures when they are done
        return len([
            future.result() for future in futures.as_completed(futures_)
        ])


if __name__ == "__main__":
    print("--> threads")
    main(download_flags_with_map(futures.ThreadPoolExecutor))
    print("--> process")
    # This is only for a try, there is no improvement in speed in general to
    # use process pool for I/O-bound tasks
    main(download_flags_with_map(futures.ProcessPoolExecutor))
    main(download_flags_with_future)
