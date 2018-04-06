import pandas as pd
from os import path

from sheep import utils


def test_data_handler_get_time_series_data():
    ticker = "SPY"
    data_dir = path.join(path.dirname(__file__), "..")
    handler = utils.CsvDataHandler(data_dir)
    df = handler.get_time_series_data(ticker)
    assert isinstance(df.index, pd.DatetimeIndex)
    assert "Close" in df.columns
