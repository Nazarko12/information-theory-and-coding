def main():
    number = 932
    print(f'Binary form of {number} is {bin(number)}')

    print('\n\t\tInverse Repetition ECC')

    irc = encode_inverse_repetition_code(number)
    print(f'Number {bin(number)} converted to inverse repetition code: {bin(irc)}')

    decoded, is_correct = decode_inverse_repetition_code(irc)
    print(f'Number in reverse repetition code {bin(irc)} is',
          [f'correct. Original number is {decoded}' if is_correct else 'incorrect!'][0])

    print('\n\t\tManchester ECC')

    mc = encode_manchester_code(number)
    print(f'Number {bin(number)} converted to Manchester code: {bin(mc)}')

    decoded, is_correct = decode_manchester_code(mc)
    print(f'Number in Manchester code {bin(mc)} is',
          [f'correct. Original number is {decoded}' if is_correct else 'incorrect!'][0])


def encode_inverse_repetition_code(number):
    bits_count = count_bits_of_number(number)
    if count_set_bits(number) % 2:
        return (number << bits_count) | inverse_number_range(number, bits_count)
    return (number << bits_count) | number


def decode_inverse_repetition_code(number):
    """Returns tuple of decoded number and data verification state (True or False)."""
    bits_count = count_bits_of_number(number)
    if bits_count % 2:
        return 0, False

    bits_count //= 2
    data_number = number >> bits_count
    check_number = number & int('1' * bits_count, 2)

    if count_set_bits(data_number) % 2:
        return data_number, data_number == inverse_number_range(check_number, bits_count)
    return data_number, data_number == check_number


def encode_manchester_code(number):
    number = bin(number)[2:]
    return int(''.join(['10' if i == '1' else '01' for i in number]), 2)


def decode_manchester_code(number):
    """Returns tuple of decoded number and data verification state (True or False)."""
    number = bin(number)[2:]
    decoded = ''
    if len(number) % 2:
        number = '0' + number

    for i in range(0, len(number), 2):
        if (number[i] + number[i + 1]) == '01':
            decoded += '0'
        elif (number[i] + number[i + 1]) == '10':
            decoded += '1'
        else:
            return 0, False
    return int(decoded, 2), True


def count_bits_of_number(number):
    count = 0
    while number:
        count += 1
        number >>= 1
    return count


def count_set_bits(number):
    """Get count of set bits in a number."""
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


def inverse_number_range(number, bits_count):
    number = bin(number)[2:]
    number = '0' * (bits_count - len(number)) + number
    return int(''.join(['1' if i == '0' else '0' for i in number]), 2)


if __name__ == '__main__':
    main()