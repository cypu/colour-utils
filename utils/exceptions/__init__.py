"""Exceptions."""


class HexadecimalColourLengthError(Exception):

    def __init__(self, hex_value):
        super(HexadecimalColourLengthError, self).__init__()
        self.message = "Hexadecimal colour should contains 6 characters. " \
                       "Optionally it can be preceded by '#'." \
                       "Your value {} has {} length".format(hex_value, len(hex_value))


class HexadecimalValueError(ValueError):

    def __init__(self, message):
        super(HexadecimalValueError, self).__init__(message)
        incorrect_value = message.split(':')[1]
        self.message = "{} value contains incorrect symbols. " \
                       "Hexadecimal system uses 0-9 and a-f symbols.".format(incorrect_value)
