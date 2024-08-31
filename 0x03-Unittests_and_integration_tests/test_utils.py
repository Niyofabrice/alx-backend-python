#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


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
