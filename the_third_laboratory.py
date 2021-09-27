def main():
    number = 932
    print(f'Binary form of {number} is {bin(number)}')

    print('\tBinary -> Gray')
    gray = binary_to_gray(number)
    print(f'Number {bin(number)} converted to Gray code: {bin(gray)}')

    print('\tGray -> Binary')
    binary = gray_to_binary(gray)
    print(f'Number in Gray code {bin(gray)} converted to binary: {bin(binary)}')


def binary_to_gray(number):
    """Convert binary to Gray code"""
    if isinstance(number, str):
        number = int(number, 2)

    return number ^ (number >> 1)


def gray_to_binary(number):
    """Convert Gray code to binary"""
    if isinstance(number, str):
        number = int(number, 2)

    mask = number >> 1
    while mask:
        number ^= mask
        mask >>= 1
    return number


if __name__ == '__main__':
    main()