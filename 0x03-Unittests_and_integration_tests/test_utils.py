""" testing unit for utils module """
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Any


class TestAccessNestedMap(unittest.TestCase):
    """ unittest for nested map access """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str], result: Any):
        """ unittest for nested map """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[str, Any],
                                         path: Tuple[str]) -> None:
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main
