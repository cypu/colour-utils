import unittest
from utils.converters import hex_to_rgb


class HexToRGBUnitTest(unittest.TestCase):

    def test_too_long_colour_string(self):

        with self.assertRaises(ValueError) as context:
            hex_to_rgb("#12423245")

        self.assertEqual("Hexadecimal colour should be in format RRGGBB", context.exception.message)

    def test_too_short_colour_string(self):

        with self.assertRaises(ValueError) as context:
            hex_to_rgb("#12423245")

        self.assertEqual("Hexadecimal colour should be in format RRGGBB", context.exception.message)

    def test_correct_length_of_colour_string(self):

        self.assertEqual(hex_to_rgb("#123456"), (18, 52, 86))
        self.assertEqual(hex_to_rgb("123456"), (18, 52, 86))
        self.assertEqual(hex_to_rgb(u"123456"), (18, 52, 86))
        self.assertEqual(hex_to_rgb(u"#123456"), (18, 52, 86))

    def test_incorrect_value(self):
        with self.assertRaises(ValueError) as context:
            hex_to_rgb("#12423245")

        self.assertEqual("Hexadecimal colour should be in format RRGGBB", context.exception.message)

    def test_incorrect_argument_type(self):

        with self.assertRaises(TypeError) as context:
            hex_to_rgb(123)

        self.assertEqual("<type 'int'> is incorrect type. Argument should be 'str' or 'unicode'", context.exception.message)

    def test_incorrect_non_hex_value(self):
        with self.assertRaises(ValueError) as context:
            l = hex_to_rgb("#ffgg11")

        self.assertEqual("invalid literal for int() with base 16: 'gg'", context.exception.message)


