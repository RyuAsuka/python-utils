keyboard_map_table = {'Q': 'A', 'W': 'B', 'E': 'C', 'R': 'D', 'T': 'E', 'Y': 'F', 'U': 'G', 'I': 'H', 'O': 'I',
                      'P': 'J', 'A': 'K', 'S': 'L', 'D': 'M', 'F': 'N', 'G': 'O', 'H': 'P', 'J': 'Q', 'K': 'R',
                      'L': 'S', 'Z': 'T', 'X': 'U', 'C': 'V', 'V': 'W', 'B': 'X', 'N': 'Y', 'M': 'Z'}

non_alph_num = ['{', '}', '(', ')', '!', '?', ',', '.', ' ', '<', '>', '/', '\\', '"', "'", '@', '#', '$', '%', '^',
                '&', '*', '[', ']', '|', ':', ';', '-', '_', '+', '=']

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'


def rot_n(text, n, skip_num=True):
    """
    The rot-n encode and decode.
    :param text: The text you want to encode or decode.
    :param n: The number that you want to change round.
    :return: The encoded or decoded string.
    """
    ret_val = ''
    for c in text:
        if c in non_alph_num:
            ret_val += c
            continue
        elif c in upper:
            temp = ord(c) + n
            if temp > ord('Z'):
                temp -= ord('Z')
                temp += ord('A') - 1
            ret_val += chr(temp)
        elif c in lower:
            temp = ord(c) + n
            if temp > ord('z'):
                temp -= ord('z')
                temp += ord('a') - 1
            ret_val += chr(temp)
        elif c in digits:
            if skip_num:
                ret_val += c
                continue
            else:
                temp = ord(c) + n
                while temp > ord('9'):
                    temp -= ord('9')
                    temp += ord('0') - 1
                ret_val += chr(temp)
    return ret_val


def barrier_encode(text, n):
    """
    The barrier encoding of original text.
    :param text: The text you want to encode
    :param n: A group with n letters
    :return: The encoded string.
    """
    arr = []
    ret_val = ''
    while text != '':
        arr.append([c for c in text[0:n]])
        text = text[n:]
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            ret_val += arr[i][j]
    return ret_val


def barrier_decode(text, n):
    """
    The barrier decode of the encrypted code.
    :param text: The encrypted text.
    :param n: The n group of text dividing.
    :return: The original text.
    """
    length = len(text)
    each_group_num = length // n
    arr = []
    ret_val = ''
    while text != '':
        arr.append([c for c in text[0:each_group_num]])
        text = text[each_group_num:]
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            ret_val += arr[i][j]
    return ret_val


def get_factors(num):
    ret_val = []
    for i in range(2, num):
        if num % i == 0:
            ret_val.append(i)
    return ret_val


def keyboard_code(text):
    """
    A map of QWERTY keyboard to Alphabet
    :param text: The original text.
    :return: The decoded text.
    """
    ret_val = ''
    for c in text:
        ret_val += keyboard_map_table[c]
    return ret_val


def test():
    # Your test code here


if __name__ == '__main__':
    test()
