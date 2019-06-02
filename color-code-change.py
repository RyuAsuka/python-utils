import sys


usage = """
Usage:
    python color-code-change.py <rgb|hex> <number>

Arguments:
    rgb: Convert RGB color to hex number style.
    hex: Convert hex number color code to RGB color number.

Examples:
    python color-code-change.py rgb 100 90 213 -> #645AD5
    python color-code-change.py hex FF9900 -> 255 153 0
"""


_hex_digits = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F']


def rgb_to_hex(r, g, b):
    result = ''
    try:
        if r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255:
            raise ValueError('RGB value should between 0 and 255.')
        for num in [r, g, b]:
            t1 = _hex_digits[num // 16]
            t2 = _hex_digits[num % 16]
            result += t1 + t2
        return '#' + result
    except ValueError as e:
        print(e)


def hex_to_rgb(hex_number):
    result = []
    try:
        if len(hex_number) != 6:
            raise ValueError('The length of HEX number must be 6!')
        t1 = hex_number[0:2]
        t2 = hex_number[2:4]
        t3 = hex_number[4:]
        for t in [t1, t2, t3]:
            assert isinstance(t, str)
            if t[0].upper() not in _hex_digits or t[1].upper() not in _hex_digits:
                raise ValueError('Invalid characters! Please check your input.')
            result.append(_hex_digits.index(t[0].upper()) * 16 + _hex_digits.index(t[1].upper()))
        return result
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(usage)
    elif sys.argv[1] == 'rgb':
        if len(sys.argv) == 5:
            result = rgb_to_hex(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
            if result is not None:
                print(result)
        else:
            print(usage)
    elif sys.argv[1] == 'hex':
        if len(sys.argv) == 3:
            result = hex_to_rgb(sys.argv[2])
            if result is not None:
                print(result)
        else:
            print(usage)
    else:
        print(usage)
