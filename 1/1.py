#!/usr/bin/python3
def find_first_digit(stuff: str) -> int:
    # returns idx of first digit
    for idx, i in enumerate(stuff):
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return int(i)
    return -1


def main() -> None:
    out = 0
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        for line in contents:
            if line:
                print(line)
                out += 10 * find_first_digit(line) + \
                    find_first_digit(line[::-1])

    print(out)


if __name__ == '__main__':
    main()
