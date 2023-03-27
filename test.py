import unittest
from string_functions import *


class TestToUpper(unittest.TestCase):
    # Tests for to_upper() function
    def test_to_upper_all_lower_case(self):
        # Test to convert all lower case characters to upper case
        self.assertEqual(to_upper("endale yohannes"), "ENDALE YOHANNES")
        self.assertTrue(to_upper("endale yohannes").isupper())
        self.assertFalse(to_upper("endale yohannes").islower())

    def test_to_upper_all_upper_case(self):
        # Test to convert all upper case characters to upper case
        self.assertEqual(to_upper("ENDALE YOHANNES"), "ENDALE YOHANNES")
        self.assertTrue(to_upper("ENDALE YOHANNES").isupper())
        self.assertFalse(to_upper("ENDALE YOHANNES").islower())

    def test_to_upper_mixed_case(self):
        # Test to convert mixed case characters to upper case
        self.assertEqual(to_upper("Endale Yohannes"), "ENDALE YOHANNES")
        self.assertTrue(to_upper("Endale Yohannes").isupper())
        self.assertFalse(to_upper("Endale Yohannes").islower())

    def test_to_upper_empty_string(self):
        # Test to convert an empty string to upper case
        self.assertEqual(to_upper(""), "")
        self.assertFalse(to_upper("").isupper())
        self.assertFalse(to_upper("").islower())


class TestToLower(unittest.TestCase):
    # Tests for to_lower() function
    def test_to_lower_all_upper_case(self):
        # Test to convert all upper case characters to lower case
        self.assertEqual(to_lower("ENDALE YOHANNES"), "endale yohannes")
        self.assertTrue(to_lower("ENDALE YOHANNES").islower())
        self.assertFalse(to_lower("ENDALE YOHANNES").isupper())

    def test_to_lower_all_lower_case(self):
        # Test to convert all lower case characters to lower case
        self.assertEqual(to_lower("endale yohannes"), "endale yohannes")
        self.assertTrue(to_lower("endale yohannes").islower())
        self.assertFalse(to_lower("endale yohannes").isupper())

    def test_to_lower_mixed_case(self):
        # Test to convert mixed case characters to lower case
        self.assertEqual(to_lower("Endale Yohannes"), "endale yohannes")
        self.assertTrue(to_lower("Endale Yohannes").islower())
        self.assertFalse(to_lower("Endale Yohannes").isupper())

    def test_to_lower_empty_string(self):
        # Test to convert an empty string to lower case
        self.assertEqual(to_lower(""), "")
        self.assertFalse(to_lower("").islower())
        self.assertFalse(to_lower("").isupper())


class TestCapitalize(unittest.TestCase):
    # Tests for capitalize() function
    def test_capitalize_all_lower_case(self):
        # Test to capitalize a string with all lower case characters
        self.assertEqual(capitalize("endale yohannes"), "Endale yohannes")
        self.assertTrue(capitalize("endale yohannes").istitle())
        self.assertFalse(capitalize("endale yohannes").isupper())

    def test_capitalize_all_upper_case(self):
        # Test to capitalize a string with all upper case characters
        self.assertEqual(capitalize("ENDALE YOHANNES"), "Endale yohannes")
        self.assertTrue(capitalize("ENDALE YOHANNES").istitle())
        self.assertFalse(capitalize("ENDALE YOHANNES").islower())

    def test_capitalize_mixed_case(self):
        # Test to capitalize a string with mixed case characters
        self.assertEqual(capitalize("EnDaLe yOhAnNeS"), "Endale yohannes")

    def test_capitalize_empty_string(self):
        # Test to capitalize an empty string
        self.assertEqual(capitalize(""), "")


if __name__ == '__main__':
    unittest.main()
