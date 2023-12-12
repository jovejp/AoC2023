from func_utils import read_file_array


input_list = read_file_array("day12.txt")


def day_12(data):
    total_steps = []
    for row_data in data:
        line_data_list = row_data.split()
        line_data = line_data_list[0]
        condition_list = [int(x) for x in line_data_list[1].split(",")]
        checked_list = [(0, 0, 0)]
        pass_simulation = 0
        while checked_list:
            cur_s, cur_c, accu_sr = checked_list.pop()
            if cur_s == len(line_data):
                if cur_c == len(condition_list) and accu_sr == 0:
                    pass_simulation += 1
                elif cur_c == len(condition_list) - 1 and accu_sr == condition_list[-1]:
                    pass_simulation += 1
            else:
                for x in [".", "#"]:
                    if line_data[cur_s] == x or line_data[cur_s] == "?":
                        if x == "." and accu_sr == 0:
                            checked_list.append((cur_s + 1, cur_c, accu_sr))
                        if x == "." and accu_sr > 0 and cur_c < len(condition_list) and accu_sr == condition_list[cur_c]:
                            checked_list.append((cur_s + 1, cur_c + 1, 0))
                        elif x == "#":
                            checked_list.append((cur_s + 1, cur_c, accu_sr + 1))

        print(line_data, condition_list, pass_simulation)
        total_steps.append(pass_simulation)
    return sum(total_steps)


if __name__ == '__main__':
    total_step = day_12(input_list)
    print(total_step)
