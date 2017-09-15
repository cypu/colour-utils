"""Gradient utils."""
from converters import hex_to_rgb


def get_linear_gradient(begin_colour, end_colour, steps):
    """Calculates linear gradient between two colours with given number of steps.
    
    :param begin_colour: hexadecimal value of begin colour
    :param end_colour: hexadecimal value of end colour
    :param steps: number of steps between begin_colour and end_colour
    :return: array of strings with hexadecimal values of colours
    """

    if not isinstance(steps, int):
        raise TypeError("{} is incorrect type. Argument should be int".format(type(steps)))

    if steps < 1:
        raise ValueError("'steps' argument should be positive. You have given: {}".format(steps))

    begin_red, begin_green, begin_blue = hex_to_rgb(begin_colour)
    end_red, end_green, end_blue = hex_to_rgb(end_colour)

    gradient = [begin_colour]

    for s in range(1, steps):
        percent = s/float(steps)
        red = int(begin_red + percent * (end_red - begin_red))
        green = int(begin_green + percent * (end_green - begin_green))
        blue = int(begin_blue + percent * (end_blue - begin_blue))
        gradient_step = "{red:02x}{green:02x}{blue:02x}".format(red=red, green=green, blue=blue)
        gradient.append(gradient_step)

    gradient.append(end_colour)

    return gradient
