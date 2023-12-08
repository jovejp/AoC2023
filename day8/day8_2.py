from collections import defaultdict
import math

def read_file_day8(file_name):
    f = open(file_name)
    action = f.readline().strip()
    action_path = defaultdict(tuple)
    line = f.readline()
    while line:
        if line.strip() != "":
            row_data = line.strip().split("=")
            action_path[row_data[0].strip()] = tuple(row_data[1].strip().replace("(","").replace(")","").split(", "))
        line = f.readline()
    f.close()
    return action, action_path


def day_7(action, action_path):
    step = 0
    cur_keys = []
    for x in action_path.keys():
        if x.endswith("A"):
            cur_keys.append(x)
    result_tuple = []
    for idx, path in enumerate(cur_keys):
        while True:
            for x in action:
                step += 1
                if x == "L":
                    cur_keys[idx] = action_path[cur_keys[idx]][0]
                else:
                    cur_keys[idx] = action_path[cur_keys[idx]][1]
                if cur_keys[idx].endswith("Z"):
                    break
            if cur_keys[idx].endswith("Z"):
                result_tuple.append(step)
                step = 0
                break
    return math.lcm(*result_tuple)


if __name__ == '__main__':
    action, action_path = read_file_day8("day8.txt")
    # print(action, action_path)
    total_step = day_7(action, action_path)
    print(total_step)
