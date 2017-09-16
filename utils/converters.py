"""Converting utils."""
from utils.exceptions import HexadecimalColourLengthError, HexadecimalValueError, HexadecimalAttributeError


def hex_to_rgb(hex_colour):
    """Converts hexadecimal colour value to RGB colour model. 
    
    :param hex_colour: hexadecimal value of colour
    :return: tuple of three elements (R, G, B)
    """

    try:
        hex_colour_stripped = hex_colour.lstrip("#")

        if len(hex_colour_stripped) != 6:
            raise HexadecimalColourLengthError(hex_colour)

        r = int(hex_colour_stripped[:2], 16)
        g = int(hex_colour_stripped[2:4], 16)
        b = int(hex_colour_stripped[4:], 16)
    except ValueError as e:
        raise HexadecimalValueError(str(e))
    except AttributeError as e:
        raise HexadecimalAttributeError(str(e))
    except HexadecimalColourLengthError:
        raise
    except:
        raise Exception("Unexpected error during conversion hexadecimal to rgb.")

    return r, g, b
