from func_utils import read_file_array_of_array
import numpy as np

import sys

sys.setrecursionlimit(2000000)

debug = False
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array_of_array(file_name)
total_rows = len(input_list)
total_cols = len(input_list[0])
print("total_rows", total_rows)
print("total_cols", total_cols)


def func():
    return 0


def part1():
    result = func()
    return result


def part2():
    result = func()
    return result


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
    r_p2 = part2()
    print("part2", r_p2)
