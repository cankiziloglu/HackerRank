import math


def main():
    decimal = int(input("decimal"))
    bin = []
    while len(bin) < 32:
        bin.insert(0, str(decimal % 2))
        decimal = math.floor(decimal / 2)

    flipped = []
    for digit in bin:
        flipped.append(str(1 - int(digit)))

    sum = 0
    for i in range(32):
        sum = sum + (int(flipped[i]) * 2 ** (31 - i))

    result = "".join(flipped)
    print("result", result)
    print("decimal", sum)


if __name__ == "__main__":
    main()
