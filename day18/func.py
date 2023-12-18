from func_utils import read_file_array

debug = False
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array(file_name)
node_list = [(0, 0)]
action_list = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def func(func_part2):
    total_steps = 0
    # get all nodes
    for row_data in input_list:
        action, step, color = row_data.split()
        if not func_part2:
            step = int(step)
            step_row, step_col = action_list[action]
        else:
            step = int(color[2:-2], 16)
            action = "RDLU"[int(color[-2:-1])]
            step_row, step_col = action_list[action]
        cur_row, cur_col = node_list[-1]
        node_list.append((cur_row + step_row * step, cur_col + step_col * step))
        total_steps += step

    # area
    total_rows = len(node_list)
    total_area = abs(sum(node_list[i][0] * (node_list[i - 1][1] - node_list[(i + 1) % total_rows][1])
                         for i in range(total_rows))) // 2
    return total_area + total_steps // 2 + 1


def part1():
    result = func(False)
    return result


def part2():
    node_list.clear()
    node_list.append((0, 0))
    result = func(True)
    return result


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
    r_p2 = part2()
    print("part2", r_p2)
