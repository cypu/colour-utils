"""Converting utils."""


def hex_to_rgb(hex_colour):
    """Converts hexadecimal colour value to RGB colour model. 
    
    :param hex_colour: hexadecimal value of colour
    :return: tuple of three elements (R, G, B)
    """

    if not (isinstance(hex_colour, str) or isinstance(hex_colour, unicode)):
        raise TypeError("{} is incorrect type. Argument should be 'str' or 'unicode'".format(type(hex_colour)))

    hex_colour = hex_colour.lstrip("#")

    if len(hex_colour) != 6:
        raise ValueError("Hexadecimal colour should be in format RRGGBB")

    try:
        r = int(hex_colour[:2], 16)
        g = int(hex_colour[2:4], 16)
        b = int(hex_colour[4:], 16)
    except ValueError as e:
        raise e

    return r, g, b
