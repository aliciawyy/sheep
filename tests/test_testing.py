from os import path, remove
import pandas as pd

from sheepts import testing


class TsTest(testing.TsTestCase):
    def setUp(self):
        self.df = pd.DataFrame(
            0.2, columns=range(2),
            index=pd.date_range("2013-01-17", "2013-01-19")
        )

    @classmethod
    def get_ref_dir(cls):
        return path.join(path.dirname(__file__), "ref")

    def test_assert_frame_equal(self):
        name = "test_assert_frame_equal"
        self.assert_frame_equal(self.df, name)

    def test_assert_ts_frame_equal(self):
        filename = path.join(path.dirname(__file__), "dummy.csv")
        testing.assert_ts_frame_equal(self.df, filename, generate_ref=True)
        assert path.exists(filename)
        testing.assert_ts_frame_equal(self.df, filename)
        remove(filename)
