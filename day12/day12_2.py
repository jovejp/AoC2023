from func_utils import read_file_array
import time

input_list = read_file_array("day12.txt")
scanned_list = {}


def find_step(line_data, condition_list, cur_s, cur_c, accu_sr):
    if (cur_s, cur_c, accu_sr) in scanned_list:
        return scanned_list[(cur_s, cur_c, accu_sr)]
    if cur_s == len(line_data):
        if cur_c == len(condition_list) and accu_sr == 0:
            return 1
        elif cur_c == len(condition_list) - 1 and accu_sr == condition_list[-1]:
            return 1
        else:
            return 0
    pass_simulation = 0
    for x in [".", "#"]:
        if line_data[cur_s] == x or line_data[cur_s] == "?":
            if x == "." and accu_sr == 0:
                pass_simulation += find_step(line_data, condition_list, cur_s + 1, cur_c, accu_sr)
            if x == "." and accu_sr > 0 and cur_c < len(condition_list) and accu_sr == condition_list[cur_c]:
                pass_simulation += find_step(line_data, condition_list, cur_s + 1, cur_c + 1, 0)
            elif x == "#":
                pass_simulation += find_step(line_data, condition_list, cur_s + 1, cur_c, accu_sr + 1)
    scanned_list[(cur_s, cur_c, accu_sr)] = pass_simulation
    return pass_simulation


def day_12(data):
    total_steps = []
    for line_data in data:
        line_data_list = line_data.split()
        base_str = (line_data_list[0] + "?") * 4 + line_data_list[0]
        condition_list = [int(x) for x in line_data_list[1].split(",")] * 5
        scanned_list.clear()
        row_steps = find_step(base_str, condition_list, 0, 0, 0)
        # print(base_str, condition_list, row_steps)
        total_steps.append(row_steps)
    return sum(total_steps)


if __name__ == '__main__':
    t = time.process_time()
    total_step = day_12(input_list)
    print(total_step)
    elapsed_time = time.process_time() - t
    print(elapsed_time)
