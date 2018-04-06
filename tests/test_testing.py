from os import path, remove
import pandas as pd
from sheepts import testing


def test_assert_ts_frame_equal():
    df = pd.DataFrame(
        0.2, columns=range(2), index=pd.date_range("2013-01-17", "2013-01-19")
    )
    filename = path.join(path.dirname(__file__), "dummy.csv")
    testing.assert_ts_frame_equal(df, filename, generate_ref=True)
    assert path.exists(filename)
    testing.assert_ts_frame_equal(df, filename)
    remove(filename)
