from func_utils import read_file_array_of_array
from collections import deque

debug = False
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array_of_array(file_name)
total_rows = len(input_list)
total_cols = len(input_list[0])
print("total_rows", total_rows)
print("total_cols", total_cols)

dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
slopes = ["^", "<", "v", ">"]
his_path = {}


def dfs(sp, p2=False):
    max_path = 1
    qw = deque()
    qw.append((1, sp, [sp]))
    while qw:
        cur_path, cur_sp, cur_moved_nodes = qw.pop()
        if cur_sp[0] == total_rows - 1:
            his_path[cur_path] = cur_moved_nodes
            break  # continue <- just lucy to find in first search
        idx = 0
        for nd in dirs:
            yy = [nd[0] + cur_sp[0], nd[1] + cur_sp[1]]
            if yy in cur_moved_nodes:
                continue
            if (input_list[yy[0]][yy[1]] in slopes
                    and (p2 or dirs[slopes.index(input_list[yy[0]][yy[1]])] == nd)):
                if idx == 0:
                    qw.append((cur_path, yy, cur_moved_nodes + [yy]))
                    idx = 1
                else:
                    max_path += 1
                    qw.append((max_path, yy, cur_moved_nodes + [yy]))
            elif input_list[yy[0]][yy[1]] == ".":
                if idx == 0:
                    qw.append((cur_path, yy, cur_moved_nodes + [yy]))
                    idx = 1
                else:
                    max_path += 1
                    qw.append((max_path, yy, cur_moved_nodes + [yy]))
    return his_path


def part1():
    all_path = dfs([0, 1], False)
    result = 0
    for x in all_path.values():
        # print(len(x))
        result = max(result, len(x))
    return result - 1


def part2():
    his_path.clear()
    all_path = dfs([0, 1], True)
    if all_path:
        result = max([len(x) for x in all_path.values()])
    else:
        result = 0
    return result - 1


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
    # r_p2 = part2()
    # print("part2", r_p2)
