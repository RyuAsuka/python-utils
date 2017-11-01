# -*- coding: utf-8 -*-
import base64
import hashlib


def urlencode(string):
    retVal = ''
    for c in string:
        retVal += hex(ord(c))
    retVal = retVal.replace('0x', '%')
    return retVal


def base64_encode(string):
    return base64.b64encode(string)


def base64_decode(string, using_hex=False):
    if not using_hex:
        return base64.b64decode(string)
    else:
        decoding = base64.b64decode(string)
        retVal = ''
        for c in decoding:
            retVal += hex(ord(c)) + ' '
        return retVal


def get_md5(string):
    return hashlib.md5(string).hexdigest()


if __name__ == '__main__':
    # Your test code here
