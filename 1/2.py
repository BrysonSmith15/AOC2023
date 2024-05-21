#!/usr/bin/python3
substring_to_val = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def find_first_last(stuff: str) -> int:
    nums = []
    for substring in substring_to_val.keys():
        try:
            nums.append((stuff.index(substring), substring_to_val[substring]))
            nums.append((len(stuff) - stuff[::-1].index(substring[::-1]) - 1,
                        substring_to_val[substring]))
        except ValueError:
            pass
    nums = sorted(list(set(nums)), key=lambda x: x[0])
    print(nums, end=' :\t')
    return 10 * nums[0][1] + nums[-1][1]


def main() -> None:
    out = 0
    with open('input', 'r') as file:
        contents = file.read().split('\n')
        for line in contents:
            if line:
                val = find_first_last(line)
                print(f'{line} : {val} : ')
                out += val
    print(out)


if __name__ == '__main__':
    main()
