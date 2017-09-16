import unittest

from utils.converters import hex_to_rgb
from utils.exceptions import HexadecimalColourLengthError, HexadecimalValueError, HexadecimalAttributeError


class HexToRGBUnitTest(unittest.TestCase):

    def test_too_long_colour_string(self):

        with self.assertRaises(Exception) as context:
            hex_value = "#12423245"
            hex_to_rgb(hex_value)

        self.assertEqual(HexadecimalColourLengthError(hex_value).message, context.exception.message)

    def test_too_short_colour_string(self):

        with self.assertRaises(Exception) as context:
            hex_value = "#12423245"
            hex_to_rgb(hex_value)

        self.assertEqual(HexadecimalColourLengthError(hex_value).message, context.exception.message)

    def test_correct_length_of_colour_string(self):

        self.assertEqual(hex_to_rgb("#123456"), (18, 52, 86))
        self.assertEqual(hex_to_rgb("123456"), (18, 52, 86))
        self.assertEqual(hex_to_rgb(u"123456"), (18, 52, 86))
        self.assertEqual(hex_to_rgb(u"#123456"), (18, 52, 86))

    def test_incorrect_argument_type(self):

        with self.assertRaises(Exception) as context:
            hex_to_rgb(123)

        self.assertEqual(HexadecimalAttributeError("object has no attribute 'lstrip").message, context.exception.message)

    def test_incorrect_non_hex_value(self):

        with self.assertRaises(Exception) as context:
            hex_to_rgb("#ffgg11")

        self.assertEqual(HexadecimalValueError("invalid literal for int() with base 16: 'gg'").message, context.exception.message)
