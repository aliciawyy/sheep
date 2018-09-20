from collections import namedtuple


def simple_coroutine(n):
    print("before")
    # yielding the value of n and wait for the value to be assigned to x
    x = yield n
    print("after: coroutine received -> x =", x)
    y = yield n + x
    print("after: coroutine received -> y =", y)


def demo_simple_coroutine():
    cor = simple_coroutine(100)
    print(cor)
    print("next ->", next(cor))
    # You can make a call to send data to a coroutine if the current coroutine
    # is suspended.
    print("send ->", cor.send(24))
    cor.send(50)


def running_average(initial):
    """
    A coroutine to compute running average.

    Examples
    --------
    >>> from inspect import getgeneratorstate
    >>> ave = running_average(10)
    >>> getgeneratorstate(ave)
    'GEN_CREATED'
    >>> next(ave)
    10.0
    >>> getgeneratorstate(ave)
    'GEN_SUSPENDED'
    >>> ave.send(20)
    15.0
    >>> ave.send(30)
    20.0

    """
    total = initial
    count = 1
    while True:
        # The yield here is used to produce the average to the caller, suspend
        # the coroutine and get a value from the caller later
        number = yield total / count
        total += number
        count += 1


def running_average_with_return(initial):
    """
    A coroutine to compute running average.

    Examples
    --------
    >>> ave = running_average_with_return(10)
    >>> next(ave)
    10.0
    >>> ave.send(20)
    15.0
    >>> ave.send(30)
    20.0
    >>> ave.send(None)
    Traceback (most recent call last):
    ...
    StopIteration: Result(total=60, count=3)
    """
    Result = namedtuple("Result", "total count")
    total = initial
    count = 1
    while True:
        # The yield here is used to produce the average to the caller, suspend
        # the coroutine and get a value from the caller later
        number = yield total / count
        if number is None:
            break
        total += number
        count += 1
    return Result(total=total, count=count)


if __name__ == "__main__":
    # demo_simple_coroutine()
    import doctest
    doctest.testmod()
