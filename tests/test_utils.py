import numpy as np

from sheepts import utils
from .mockutils import MockTsTestCase


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


class ApplyTest(MockTsTestCase):
    def test_apply_by_multiprocessing(self):
        df = self.data_handler.get_time_series_data("SPY")
        df = df.loc["2010", ["Open", "Close", "High", "Low"]]
        res_no_parallel = df.apply(np.mean, axis=1)
        res_parallel = utils.apply_by_multiprocessing(
            df, np.mean, n_cpu=2, axis=1
        )
        self.assert_pd_series_equal(res_no_parallel, res_parallel)
