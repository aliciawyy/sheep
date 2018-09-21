"""
The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

- ThreadPoolExecutor is an Executor subclass that uses a pool of threads
to execute calls asynchronously.
- The ProcessPoolExecutor class is an Executor subclass that uses a pool of
processes to execute calls asynchronously.

Run the script with

$ python -m futures.flag_sequential

"""
from concurrent import futures

from .flag_sequential import main, download_flag

MAX_WORKERS = 20


def download_flags_async(executor):
    """
     The exc.__exit__ calls the exc.shutdown(wait=True), which will block till
    all threads/processes are done.
    """
    def download_flags_threads(countries):
        with executor(MAX_WORKERS) as exc:
            return len(list(exc.map(download_flag, countries)))
    return download_flags_threads


if __name__ == "__main__":
    print("--> threads")
    main(download_flags_async(futures.ThreadPoolExecutor))
    print("--> process")
    main(download_flags_async(futures.ProcessPoolExecutor))
