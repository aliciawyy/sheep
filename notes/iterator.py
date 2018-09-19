"""
# Iterable vs Iterator vs Generator

- s is an iterable whose method __iter__ instantiates a new iterator every time.
- t is an iterator for whom the method __iter__ returns self

## Generator

Any Python function that has the `yield` keyword in its body is a generator
function, which, when called, returns a generator object.

A generator function builds a generator object that wraps the body of the function.
When we invoke `next(...)` on the generator object, execution advances to the
next `yield` in the function body to evaluate the value yielded. Finally when
the function body returns, the generator object raises a `StopIteration` in
accordance with the iterator protocol.

The iterator interface is designed to be lazy.
A generator is considered as a lazy implementation as it postpones producing
values to the last possible moment. This saves memory and may avoid useless
processing as well.

An iterator traverses a collection and yields items from it. While a generator
may produce values without necessarily traversing a collection.
"""
s = "ABC"

t = iter(s)
print(repr(t))
print(repr(iter(t)))

while True:
    try:
        print(next(t))
    except StopIteration as e:
        print(repr(e))
        break
