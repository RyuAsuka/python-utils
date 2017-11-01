MORES_TABLE = {'.-':    'A',
               '-...':  'B',
               '-.-.':  'C',
               '-..':   'D',
               '.':     'E',
               '..-.':  'F',
               '--.':   'G',
               '....':  'H',
               '..':    'I',
               '.---':  'J',
               '-.-':   'K',
               '.-..':  'L',
               '--':    'M',
               '-.':    'N',
               '---':   'O',
               '.--.':  'P',
               '--.-':  'Q',
               '.-.':   'R',
               '...':   'S',
               '-':     'T',
               '..-':   'U',
               '...-':  'V',
               '.--':   'W',
               '-..-':  'X',
               '-.--':  'Y',
               '--..':  'Z',
               '.----': '1',
               '..---': '2',
               '...--': '3',
               '....-': '4',
               '.....': '5',
               '-....': '6',
               '--...': '7',
               '---..': '8',
               '----.': '9',
               '-----': '0'}


def convert_mores_alphabet(mores_string):
    words = mores_string.split('/')
    final_words = []
    for word in words:
        w = ''
        chars = word.split(' ')
        for c in chars:
            w += MORES_TABLE[c]
        final_words.append(w)
    return final_words


if __name__ == '__main__':
    input = '-.-/../--.-/.-../.--/-/..-./-.-./--.-/--./-./.../---/---'
    output = convert_mores_alphabet(input)
    o2 = ''
    for i in output:
        o2 += i
    print o2
