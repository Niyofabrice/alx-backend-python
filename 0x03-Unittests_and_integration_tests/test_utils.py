#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Function to test access_nested_map
        Args:
            nested_map: Dict containing the map
            path: Tuple of the path to go through
            expected_result: Dict int
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """
        Function that test for exceptions on access_nested_map
        Args:
            nested_map: Dict containing the map
            path: Tuple of the path to go through
            exception: Exception name
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Function that test for ex on get_json without requesting a actual HTTP
        Args:
            test_url: url to send request to
            payload: payload
            mock_get: mock object
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        res = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(res, test_payload)
        mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """
    Memoize test class
    """
    def test_memoize(self):
        """
        Function to test memoize
        """
        class TestClass:

            def a_method(self):
                """
                Function that returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                Function calling a_method
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as m_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            m_method.assert_called_once()
