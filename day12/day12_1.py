from func_utils import read_file_array
import time

input_list = read_file_array("day12.txt")


def day_12(data):
    total_steps = []
    for idx, row_data in enumerate(data):
        line_data_list = row_data.split()
        line_data = (line_data_list[0] + "?") * 4 + line_data_list[0]
        condition_list = [int(x) for x in line_data_list[1].split(",")] * 5
        checked_list = [(0, 0, 0)]
        processed_list = {}
        while checked_list:
            key = checked_list.pop()
            if key in processed_list.keys():
                continue
            cur_s, cur_c, accu_sr = key
            if cur_s == len(line_data):
                if cur_c == len(condition_list) and accu_sr == 0:
                    processed_list[(cur_s, cur_c, accu_sr)] = 1
                elif cur_c == len(condition_list) - 1 and accu_sr == condition_list[-1]:
                    processed_list[(cur_s, cur_c, accu_sr)] = 1
                else:
                    processed_list[(cur_s, cur_c, accu_sr)] = 0
            elif cur_s < len(line_data):
                next_list = []
                for x in [".", "#"]:
                    if line_data[cur_s] == x or line_data[cur_s] == "?":
                        if x == "." and accu_sr == 0:
                            checked_list.append((cur_s + 1, cur_c, accu_sr))
                            next_list.append(checked_list[-1])
                        elif (x == "." and accu_sr > 0 and cur_c < len(condition_list)
                              and accu_sr == condition_list[cur_c]):
                            checked_list.append((cur_s + 1, cur_c + 1, 0))
                            next_list.append(checked_list[-1])
                        elif x == "#":
                            checked_list.append((cur_s + 1, cur_c, accu_sr + 1))
                            next_list.append(checked_list[-1])
                processed_list[(cur_s, cur_c, accu_sr)] = next_list
        while not isinstance(processed_list[(0, 0, 0)], int):
            for k, v in processed_list.items():
                if isinstance(v, int):
                    pass
                elif all(isinstance(processed_list[x], int) for x in v):
                    processed_list[k] = sum([processed_list[x] for x in v])
        print(idx, processed_list[(0, 0, 0)])
        total_steps.append(processed_list[(0, 0, 0)])
    return sum(total_steps)


if __name__ == '__main__':
    t = time.process_time()
    total_step = day_12(input_list)
    print(total_step)
    elapsed_time = time.process_time() - t
    print(elapsed_time)
