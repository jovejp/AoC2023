from func_utils import read_file_array_of_array
from collections import deque
import numpy as np

debug = False
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array_of_array(file_name)
total_rows = len(input_list)
total_cols = len(input_list[0])
for idx, x in enumerate(input_list):
    if 'S' in x:
        print(idx, x.index('S'))
        start_cell = (idx, x.index('S'))
        break
print("total_rows", total_rows)
print("total_cols", total_cols)
moveable_area = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def func(steps):
    i = 0
    visited_node = set()
    cur_process = [start_cell]
    next_process = []
    visited_node_his = {}
    while i <= steps:
        visited_node_his[i] = cur_process.copy()
        print(i, len(visited_node_his[i]), visited_node_his[i])
        while cur_process:
            # print("step", i, "process_node", cur_process)
            cur_node = cur_process.pop()
            visited_node.add(tuple(cur_node))
            for xx in moveable_area:
                next_xx, next_yy = cur_node[0] + xx[0], cur_node[1] + xx[1]
                if (0 <= next_xx < total_rows and 0 <= next_yy < total_cols and input_list[next_xx][next_yy] != "#"
                        and [next_xx, next_yy] not in next_process and tuple([next_xx, next_yy]) not in visited_node):
                    next_process.append([next_xx, next_yy])
        cur_process = next_process.copy()
        next_process.clear()
        i += 1

    total_steps = 0
    for xx in range(len(visited_node_his)):
        if xx <= steps and xx % 2 == 0:
            total_steps += len(visited_node_his[xx])

    return total_steps


def part1():
    result = func(64)
    return result


def part2():
    result = func()
    return result


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
    # r_p2 = part2()
    # print("part2", r_p2)
