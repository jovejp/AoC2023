from func_utils import read_file_array_of_array
import heapq

debug = True
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array_of_array(file_name)
total_rows = len(input_list)
total_cols = len(input_list[0])
print("total_rows", total_rows)
print("total_cols", total_cols)
move_dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]


def func(min_step, max_step, part):
    path_values = {}
    process_deque = [(0, 0, 0, 2, 0)]

    while process_deque:
        path_total, x, y, z, step = heapq.heappop(process_deque)
        if (x, y, z, step) in path_values:
            continue
        path_values[(x, y, z, step)] = path_total
        for i, (mr, mc) in enumerate(move_dir):
            nx = x + mr
            ny = y + mc

            nz = i
            ns = step + 1 if z == nz else 1
            chk_part1 = (ns <= max_step)
            chk_bound = ((i == 0 and ny + 1 >= min_step) or (i == 1 and nx + 1 >= min_step) or
                         (i == 2 and total_cols - ny >= min_step) or (i == 3 and total_rows - nx >= min_step))
            chk_part2 = ns <= max_step and (z == nz or step >= min_step or step == 0) and (ns != 1 or chk_bound)
            chk_all = chk_part2 if part else chk_part1
            if 0 <= nx < total_rows and 0 <= ny < total_cols and chk_all and (z != (nz + 2) % 4):
                heapq.heappush(process_deque, (path_total + int(input_list[nx][ny]), nx, ny, nz, ns))
    result = [10000]
    for k, v in path_values.items():
        x, y, z, step = k
        if x == total_rows - 1 and y == total_cols - 1:
            result.append(v)

    return min(result)


def part1():
    result = func(0, 3, False)
    return result


def part2():
    result = func(4, 10, True)
    return result


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
    r_p2 = part2()
    print("part2", r_p2)
