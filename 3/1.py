#!/usr/bin/python3
from string import punctuation
from typing import List, Tuple


dirs = [
    (i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)
]


def is_adjacent(row: int, col: int, schematic: str) -> bool:
    rows = schematic.split('\n')
    new_positions = list(filter(
        lambda p: 0 <= p[0] and p[0] < len(schematic)
        and 0 <= p[1] and p[1] < len(
            schematic.split('\n')[0]), [(row + i, col + j) for i, j in dirs]))
    print(str((row, col)) + '\t', *
          [rows[new[0]][new[1]] for new in new_positions])
    for new in new_positions:
        if rows[new[0]][new[1]] in punctuation and rows[new[0]][new[1]] != '.':
            return True
    return False


def get_numbers(schematic: str) -> List[Tuple[int, int, int, int]]:
    # returns [(Number, Row, StartCol, EndCol)]
    nums = []
    rows = schematic.split('\n')
    for ridx, row in enumerate(rows):
        in_number = False
        start_num = -1
        curr_num = []
        for cidx, col in enumerate(row):
            if col in '0123456798':
                if not in_number:
                    start_num = cidx
                    in_number = True
                curr_num.append(int(col))
            else:
                if in_number:
                    curr_sum = 0
                    for idx, val in enumerate(curr_num[::-1]):
                        curr_sum += (10 ** idx) * val
                    nums.append((curr_sum, ridx, start_num, cidx - 1))
                    curr_num = []
                in_number = False
    return nums


def main() -> None:
    with open('input', 'r') as file:
        schematic = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
        nums = get_numbers(schematic)
        sum = 0
        for num in nums:
            for col in range(num[1], num[2] + 1):
                if is_adjacent(num[1], col, schematic):
                    print(num[0])
                    sum += num[0]
                    break
        print(sum)


if __name__ == '__main__':
    main()
