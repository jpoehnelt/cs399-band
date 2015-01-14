from unittest import TestCase
from cs399 import cs399


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(cs399.run))
