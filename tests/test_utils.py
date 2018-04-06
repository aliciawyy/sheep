from sheepts import utils


def test_lazy_property():
    class LazyProp(object):
        def __init__(self):
            self.call_count = 0

        @utils.lazy_property
        def a(self):
            """Lazy a"""
            self.call_count += 1
            return "so_lazy"

    lp = LazyProp()
    for _ in range(5):
        assert "so_lazy" == lp.a
    assert 1 == lp.call_count
    assert "Lazy a" == LazyProp.a.__doc__


def test_string_mixin_repr():
    class A(utils.StringMixin):
        def __init__(self):
            self.a = list(range(50))
            self.b = "b"

    assert "A(b='b')" == str(A())
