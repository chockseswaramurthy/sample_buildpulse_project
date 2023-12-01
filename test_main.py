import unittest
from typing import List

from parameterized import parameterized

from .main import get_numbers


class RandomNumberTestCase(unittest.TestCase):
    @parameterized.expand([
        ([1, 2], '')
    ])
    def test_get_numbers_flaky(self, expected_list: List[int], _):
        self.assertListEqual(get_numbers(), expected_list)

    @parameterized.expand([
        ([1, 2], '')
    ])
    def test_get_numbers_good(self, expected_list: List[int], _):
        self.assertListEqual(sorted(get_numbers()), sorted(expected_list))


if __name__ == '__main__':
    unittest.main()
