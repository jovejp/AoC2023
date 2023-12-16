from func_utils import read_file_array_of_array
from collections import defaultdict
import numpy as np

debug = False
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array_of_array(file_name)
total_rows = len(input_list)
total_cols = len(input_list[0])
print("total_rows", total_rows)
print("total_cols", total_cols)
input_list = np.array(input_list)
wait_list = []
moved_history = defaultdict(np.ndarray)


def move(start_point, update_list, moved_action):
    moved_action.append(start_point)
    x, y, z = start_point
    if x >= 0 and y >= 0:
        update_list[x][y] = "#"
    if z == 'r' and y < total_cols - 1:
        if input_list[x][y + 1] in [".", "-"]:
            wait_list.append((x, y + 1, 'r'))
        elif input_list[x][y + 1] == "\\":
            wait_list.append((x, y + 1, 'd'))
        elif input_list[x][y + 1] == "/":
            wait_list.append((x, y + 1, 'u'))
        elif input_list[x][y + 1] == "|":
            wait_list.append((x, y + 1, 'u'))
            wait_list.append((x, y + 1, 'd'))
    elif z == 'l' and y > 0:
        if input_list[x][y - 1] in [".", "-"]:
            wait_list.append((x, y - 1, 'l'))
        elif input_list[x][y - 1] == "\\":
            wait_list.append((x, y - 1, 'u'))
        elif input_list[x][y - 1] == "/":
            wait_list.append((x, y - 1, 'd'))
        elif input_list[x][y - 1] == "|":
            wait_list.append((x, y - 1, 'u'))
            wait_list.append((x, y - 1, 'd'))
    elif z == 'd' and x < total_rows - 1:
        if input_list[x + 1][y] in [".", "|"]:
            wait_list.append((x + 1, y, 'd'))
        elif input_list[x + 1][y] == "\\":
            wait_list.append((x + 1, y, 'r'))
        elif input_list[x + 1][y] == "/":
            wait_list.append((x + 1, y, 'l'))
        elif input_list[x + 1][y] == "-":
            wait_list.append((x + 1, y, 'l'))
            wait_list.append((x + 1, y, 'r'))
    elif z == 'u' and x > 0:
        if input_list[x - 1][y] in [".", "|"]:
            wait_list.append((x - 1, y, 'u'))
        elif input_list[x - 1][y] == "\\":
            wait_list.append((x - 1, y, 'l'))
        elif input_list[x - 1][y] == "/":
            wait_list.append((x - 1, y, 'r'))
        elif input_list[x - 1][y] == "-":
            wait_list.append((x - 1, y, 'l'))
            wait_list.append((x - 1, y, 'r'))
    elif not z:
        print("direction wrong!!!", x, y, z)


def part1():
    update_list = input_list.copy()
    moved_action = []
    wait_list.append((0, -1, 'r'))
    while wait_list:
        start_point = wait_list.pop()
        if start_point not in moved_action:
            move(start_point, update_list, moved_action)
    return (update_list == "#").sum()


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
