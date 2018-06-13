from os import path

from sheepts.testing import TsTestCase
from sheepts.data import CsvDataHandler


class MockTsTestCase(TsTestCase):
    @classmethod
    def setUpClass(cls):
        super(MockTsTestCase, cls).setUpClass()
        cls.data_dir = path.join(path.dirname(__file__), "data")
        cls.data_handler = CsvDataHandler(cls.data_dir)

    @classmethod
    def get_ref_dir(cls):
        return path.join(path.dirname(__file__), "ref")
