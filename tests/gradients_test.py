import unittest
from utils.gradients import get_linear_gradient


class GetLinearGradientTestCase(unittest.TestCase):

    def test_wrong_number_of_steps(self):

        with self.assertRaises(ValueError) as context:
            get_linear_gradient("ffffff", '000000', 0)

        self.assertEqual("'steps' argument should be positive. You have given: 0", context.exception.message)

    def test_wrong_type_of_steps_argument(self):

        with self.assertRaises(TypeError) as context:
            get_linear_gradient("ffffff", '000000', "6")

        self.assertEqual("<type 'str'> is incorrect type. Argument should be int", context.exception.message)

    def test_get_gradient_with_steps(self):

        self.assertEqual(get_linear_gradient("ffffff", '000000', 1), ['ffffff', '000000'])
        self.assertEqual(get_linear_gradient("000000", 'ffffff', 1), ['000000', 'ffffff'])
        self.assertEqual(get_linear_gradient("ffffff", '000000', 5), ['ffffff', 'cccccc', '999999', '666666', '333333', '000000'])
        self.assertEqual(get_linear_gradient("000000", 'ffffff', 6), ['000000', '2a2a2a', '555555', '7f7f7f', 'aaaaaa', 'd4d4d4', 'ffffff'])
        self.assertEqual(get_linear_gradient("ff12d3", '00ee12', 4), ['ff12d3', 'bf49a2', '7f8072', '3fb742', '00ee12'])






