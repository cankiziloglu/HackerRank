import math


def flippingBits(n):
    bin = []
    while len(bin) < 32:
        bin.insert(0, str(n % 2))
        n = math.floor(n / 2)

    flipped = []
    for digit in bin:
        flipped.append(str(1 - int(digit)))

    sum = 0
    for i in range(32):
        sum = sum + (int(flipped[i]) * 2 ** (31 - i))

    return sum
