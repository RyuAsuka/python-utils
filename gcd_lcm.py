def gcd(a, b):
    if a > b:
        (a, b) = (b, a)
    r = b % a
    if r == 0:
        return a
    else:
        return gcd(a, r)


def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


if __name__ == '__main__':
    print(gcd(115, 125))
    print(lcm(100, 125))
