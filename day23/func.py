from func_utils import read_file_array_of_array
from collections import deque

debug = True
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array_of_array(file_name)
total_rows = len(input_list)
total_cols = len(input_list[0])
print("total_rows", total_rows)
print("total_cols", total_cols)

dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
slopes = ["<^>v"]
his_path = {}


def dfs(sp):
    max_path = 1
    qw = deque()
    qw.append((1, sp, []))
    while qw:
        cur_path, cur_sp, cur_moved_nodes = qw.pop()
        # print("new round started:", cur_path, cur_sp, cur_moved_nodes)
        if cur_sp[0] == total_rows - 1:
            his_path[cur_path] = cur_moved_nodes
            continue
        if input_list[cur_sp[0]][cur_sp[1]] in slopes:
            nd = dirs[slopes.index(input_list[sp[0]][sp[1]])]
            ns = [a + b for a, b in zip(cur_sp, nd)]
            if input_list[ns[0]][ns[1]] == ".":
                qw.append((cur_path, ns, cur_moved_nodes + [ns]))
            else:
                print("this way is blocked!!!", cur_path, ns, cur_moved_nodes)
        else:
            ns = [[nd[0] + cur_sp[0], nd[1] + cur_sp[1]] for nd in dirs
                  if input_list[nd[0] + cur_sp[0]][nd[1] + cur_sp[1]] != "#"
                  and [nd[0] + cur_sp[0], nd[1] + cur_sp[1]] not in cur_moved_nodes]

            # print("cur_path, cur_sp, ns", cur_path, cur_sp, ns)

            for idx, yy in enumerate(ns):
                if idx == 0:
                    qw.append((cur_path, yy, cur_moved_nodes + [yy]))
                else:
                    max_path += 1
                    qw.append((max_path, yy, cur_moved_nodes + [yy]))
    return his_path


def part1():
    all_path = dfs([0, 1])
    result = max([len(x) for x in all_path.values()])
    return result


def part2():
    all_path = dfs([0, 1])
    result = max([len(x) for x in all_path.values()])
    return result


if __name__ == '__main__':
    # r_p1 = part1()
    # print("part1", r_p1)
    r_p2 = part2()
    print("part2", r_p2)
