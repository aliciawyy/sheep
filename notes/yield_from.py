from collections import namedtuple


def averager():
    """

    >>> ave = averager()
    >>> next(ave)
    >>> ave.send(10)
    10.0
    >>> ave.send(15)
    12.5

    """
    Result = namedtuple("Result", "count average")
    total = 0
    count = 0
    average = 0.
    while True:
        number = yield average
        if number is None:
            result = Result(count=count, average=average)
            print("averager return result ->", result)
            return result
        total += number
        count += 1
        average = total / count


def grouper(result, key):
    """

    grouper is a delegating generator that works as a pipe between the client
    method `main` and the subgenerator `averager`

    """
    while True:
        print("before run grouper with key ->", key, result)
        result[key] = yield from averager()
        print("after run grouper with key ->", key, result)


def main(data):
    """
    We notice that the grouper loop is called twice per key
    >>> data = {"girl": [10, 15, 30, 20], "boy": [4, 5, 9]}
    >>> main(data)
    {'girl': Result(count=4, average=18.75), 'boy': Result(count=3, average=6.0)}
    """
    result = {}
    for key, values in data.items():
        group = grouper(result, key)
        print(next(group))
        print("after next")
        for v in values:
            group.send(v)
        # sending None into group causes the current averager instance to
        # terminate. If a subgenerator never terminates, the delegating
        # generator will suspended forever at the `yield from`.
        print("before sending None for key ->", key)
        group.send(None)  # close the channel
        print("after sending None for key ->", key)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
