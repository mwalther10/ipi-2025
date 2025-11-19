def hex_to_dec(hex: str) -> int:
    """Convert a hexadecimal number to its decimal equivalent.

    Args:
        hex (str): A string representing a hexadecimal number (e.g., 'FF').

    Returns:
        int: The decimal equivalent of the hexadecimal number.
    """
    decimal = 0
    hex_digits = '0123456789ABCDEF'
    for index, char in enumerate(reversed(hex)):
        value = hex_digits.index(char)
        decimal += value * (16 ** index)
    return decimal

# Version ohne index und reversed
#    decimal = 0
#    hex_digits = '0123456789ABCDEF'
#    length = len(hex)
#    for i in range(length):
#        char = hex[length - 1 - i]
#        value = hex_digits.index(char)
#        decimal += value * (16 ** i)
#    return decimal

assert hex_to_dec("0") == 0
assert hex_to_dec("17") == 23
assert hex_to_dec("FF") == 255
assert hex_to_dec("00FF") == 255
assert hex_to_dec("3AF2") == 15090

def parse_color(color: str) -> tuple[int, int, int]:
    """Parse a color in hexadecimal format to its RGB components.

    Args:
        color (str): A string representing a color in hexadecimal format
                     (e.g., 'RRGGBB'). 
    Returns:
        tuple[int, int, int]: A tuple containing the red, green, and blue
                                components as integers.
    """
    red_hex = color[0:2]
    green_hex = color[2:4]
    blue_hex = color[4:6]
    red = hex_to_dec(red_hex)
    green = hex_to_dec(green_hex)
    blue = hex_to_dec(blue_hex)
    return (red, green, blue)

assert parse_color("000000") == (0, 0, 0)
assert parse_color("FFFFFF") == (255, 255, 255)
assert parse_color("FA7BCC") == (250, 123, 204)
assert parse_color("123456") == (18, 52, 86)