from collections import defaultdict


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
    cur_key = "AAA"
    while True:
        for x in action:
            if x == "L":
                cur_key = action_path[cur_key][0]
            else:
                cur_key = action_path[cur_key][1]
            step += 1
            if cur_key == "ZZZ":
                break
        if cur_key == "ZZZ":
            break
    return step


if __name__ == '__main__':
    action, action_path = read_file_day8("day8.txt")
    total_step = day_7(action, action_path)
    print(total_step)
