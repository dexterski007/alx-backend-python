""" testing unit for utils module """
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock
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
        """ test for access nested map exception """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ unittest for json class """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, Any], mock_get: Mock) -> None:
        """ tester for get_json method """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """unittest for testing memoization """
    def test_memoize(self):
        """ test memoize method """
        class TestClass:
            """ test class for mock """
            def a_method(self):
                """ method that return the ultimate number """
                return 42

            @memoize
            def a_property(self):
                """ method that returns the method """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            tested_class = TestClass()
            self.assertEqual(tested_class.a_property, 42)
            self.assertEqual(tested_class.a_property, 42)
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
