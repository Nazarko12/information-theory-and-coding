def main():
    number = 932
    print(f'Binary form of {number} is {bin(number)}\n')

    hc = convert_to_hamming_code(number)
    print(f'Number {bin(number)} converted to Hamming code: {bin(hc)}')

    decoded = convert_from_hamming_code_with_correction(hc)
    print(f'Number in Hamming code {bin(hc)} converted to original: {bin(decoded)} or {decoded}')

    print('\n\tCorrection Test')
    hc ^= 1 << 4
    decoded = convert_from_hamming_code_with_correction(hc)
    print(f'Hamming code with 5th bit set wrong {bin(hc)} converted to original: {bin(decoded)} or {decoded}')
    if decoded == number:
        print('Correction completed successfully!')


def convert_to_hamming_code(number):
    if isinstance(number, int):
        number = bin(number)[2:]

    number = list(number[::-1])
    check_bits_quantity = get_check_bits_quantity(data_length=len(number))
    for i in range(check_bits_quantity):
        number.insert(2 ** i - 1, '?')

    for i in range(check_bits_quantity):
        sequence = []
        for j in range(2 ** i - 1, len(number), 2 ** (i + 1)):
            sequence += number[j: j + 2 ** i]
        number[2 ** i - 1] = str(count_set_bits(int(''.join(sequence[1:]), 2)) % 2)

    number = ''.join(number[::-1])
    return int(number, 2)


def convert_from_hamming_code_with_correction(number):
    if isinstance(number, int):
        number = bin(number)[2:]

    number = list(number[::-1])
    check_bits_quantity = get_check_bits_quantity(full_length=len(number))
    check_bits_indices = [2 ** i - 1 for i in range(check_bits_quantity)]

    data = []
    check = []
    for i in range(len(number)):
        if i in check_bits_indices:
            check.append(number[i])
        else:
            data.append(number[i])

    decoded = list(bin(convert_to_hamming_code(data[::-1]))[2:][::-1])
    if decoded != number:
        decoded_check = []
        for i in range(check_bits_quantity):
            decoded_check.append(decoded[2 ** i - 1])
        wrong_bit = 0
        for i, j, k in zip(range(check_bits_quantity), check, decoded_check):
            if j != k:
                wrong_bit += 2 ** i
        if number[wrong_bit - 1] == '0':
            number[wrong_bit - 1] = '1'
        else:
            number[wrong_bit - 1] = '0'
        data = convert_from_hamming_code_with_correction(''.join(number[::-1]))

    if isinstance(data, int):
        return data
    number = ''.join(data[::-1])
    return int(number, 2)


def get_check_bits_quantity(data_length=None, full_length=None):
    if full_length is None:
        for i in range(data_length):
            if 2 ** i >= data_length + i + 1:
                return i
    for i in range(full_length):
        if 2 ** i >= full_length + 1:
            return i


def count_set_bits(number):
    if isinstance(number, str):
        number = int(number, 2)

    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


if __name__ == '__main__':
    main()