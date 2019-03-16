import sys


# Order
# 1 2 3
# 4 5 6
# 7 8 9
def to_digit(binary):
    if binary == '000001001':
        return 1
    elif binary == '010011110':
        return 2
    elif binary == '010011011':
        return 3
    elif binary == '000111001':
        return 4
    elif binary == '010110011':
        return 5
    elif binary == '010110111':
        return 6
    elif binary == '010001001':
        return 7
    elif binary == '010111111':
        return 8
    elif binary == '010111001':
        return 9
    elif binary == '010101111':
        return 0
    return -1


def to_binary(string):
    return ''.join(['0' if char == ' ' else '1' for char in string])


# Converts ['|_|  _ ' to ['111', 010']
def splice(string):
    return [to_binary(string[x:x+3]) for x in range(0, len(string), 4)]


def parse(string):
    # Split into 3 lines
    lines = string.splitlines()

    # Separate each one of them by binary strings of length 3
    first_line_segments = splice(lines[0])
    second_line_segments = splice(lines[1])
    third_line_segments = splice(lines[2])

    digit_count = len(first_line_segments)

    # Merge all three sets to get full binary string
    full_segments = [first_line_segments[x] + second_line_segments[x] + third_line_segments[x]
                     for x in range(digit_count)]

    return ''.join([str(to_digit(x)) for x in full_segments])


def main():
    with open(sys.argv[1], 'r') as f:
        print(parse(f.read()))


if __name__ == '__main__':
    main()
