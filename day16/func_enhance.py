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
input_list = np.array(input_list)
moved_history = {}
move_list_action = set()
move_list = set()
row_acts = ['l', 'r']
col_acts = ['u', 'd']


def next_action(cur_act, mirror):
    if mirror == "/":
        if cur_act in row_acts:
            next_act = col_acts[1 ^ row_acts.index(cur_act)]
        else:
            next_act = row_acts[1 ^ col_acts.index(cur_act)]
    elif mirror == "\\":
        if cur_act in row_acts:
            next_act = col_acts[row_acts.index(cur_act)]
        else:
            next_act = row_acts[col_acts.index(cur_act)]
    elif mirror == "|":
        if cur_act in row_acts:
            next_act = col_acts
        else:
            next_act = cur_act
    elif mirror == "-":
        if cur_act in col_acts:
            next_act = row_acts
        else:
            next_act = cur_act
    else:
        next_act = cur_act
    return next_act


def simu_steps(start_point):
    if start_point in move_list_action:
        return 0
    else:
        move_list_action.add(start_point)
    (x, y, z) = start_point
    if x >= 0 and y >= 0:
        if (x, y) in move_list:
            step = 0
        else:
            step = 1
            move_list.add((x, y))
    else:
        step = 0
    if z == 'r' and y < total_cols - 1:
        next_x = x
        next_y = y + 1
    elif z == 'l' and y > 0:
        next_x = x
        next_y = y - 1
    elif z == 'd' and x < total_rows - 1:
        next_x = x + 1
        next_y = y
    elif z == 'u' and x > 0:
        next_x = x - 1
        next_y = y
    else:
        moved_history[start_point] = step
        return step

    acts = next_action(z, input_list[next_x][next_y])
    if isinstance(acts, list):
        for act in acts:
            step += simu_steps((next_x, next_y, act))
    else:
        step += simu_steps((next_x, next_y, acts))
    # print(start_point, step)
    moved_history[start_point] = step
    return step


def part1():
    total_step = simu_steps((0, -1, 'r'))
    return total_step


def part2():
    result_list = []
    for x in range(total_rows):
        move_list_action.clear()
        move_list.clear()
        moved_history.clear()
        result = simu_steps((x, -1, 'r'))
        # print(x, -1, result)
        result_list.append(result)

    for x in range(total_rows):
        move_list_action.clear()
        move_list.clear()
        moved_history.clear()
        result = simu_steps((x, total_cols, 'l'))
        # print(x, total_cols, result)
        result_list.append(result)
    for x in range(total_cols):
        move_list_action.clear()
        move_list.clear()
        moved_history.clear()
        result = simu_steps((-1, x, 'd'))
        # print(-1, x, result)
        result_list.append(result)
    for x in range(total_cols):
        move_list_action.clear()
        move_list.clear()
        moved_history.clear()
        result = simu_steps((total_rows, x, 'u'))
        # print(total_rows, x, result)
        result_list.append(result)
    return max(result_list)


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
    r_p2 = part2()
    print("part2", r_p2)
