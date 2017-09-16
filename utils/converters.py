"""Converting utils."""
from utils.exceptions import HexadecimalColourLengthError, HexadecimalValueError


def hex_to_rgb(hex_colour):
    """Converts hexadecimal colour value to RGB colour model. 
    
    :param hex_colour: hexadecimal value of colour
    :return: tuple of three elements (R, G, B)
    """

    if not (isinstance(hex_colour, str) or isinstance(hex_colour, unicode)):
        raise TypeError("{} is incorrect type. Argument should be 'str' or 'unicode'".format(type(hex_colour)))

    hex_colour_stripped = hex_colour.lstrip("#")

    if len(hex_colour_stripped) != 6:
        raise HexadecimalColourLengthError(hex_colour)

    try:
        r = int(hex_colour_stripped[:2], 16)
        g = int(hex_colour_stripped[2:4], 16)
        b = int(hex_colour_stripped[4:], 16)
    except ValueError as e:
        raise HexadecimalValueError(str(e))

    return r, g, b
