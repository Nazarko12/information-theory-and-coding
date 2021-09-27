def main():
    number = 932
    print(f'Binary form of {number} is {bin(number)}')

    print('\tAdd parity bit')
    number_with_parity_bit = add_parity_bit(number)
    print(f'Number {bin(number)} with added parity bit: {bin(number_with_parity_bit)}')

    print('\tCheck parity bit')
    is_correct = check_parity_bit(number_with_parity_bit)
    print(f'Number with parity bit {bin(number_with_parity_bit)} is',
          [f'correct. Original number is {number_with_parity_bit >> 1}' if is_correct else 'incorrect!'][0])


def add_parity_bit(number):
    """Set first bit of number as a parity bit."""
    return (number << 1) | (count_set_bits(number) % 2)


def check_parity_bit(number):
    """
    :param number: number with first bit as a parity bit
    :return: True if parity check is successful
    """
    return not count_set_bits(number) % 2


def count_set_bits(number):
    """Get count of set bits in a number."""
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count


if __name__ == '__main__':
    main()