from collections import defaultdict
import numpy as py


def read_file_day6(file_name):
    line_data = defaultdict(list)
    f = open(file_name)
    line_data["time"] = [int(x) for x in (f.readline().split(":")[1].split())]
    line_data["distance"] = [int(x) for x in (f.readline().split(":")[1].split())]
    f.close()
    return line_data


def day_6(main_list):
    times = main_list["time"]
    dists = main_list["distance"]
    result_list = []
    for index, time in enumerate(times):
        count = 0
        for x in range(time):
            if x * (time - x) > dists[index]:
                count += 1
            else:
                if count > 0:
                    break
        result_list.append(count)
    return py.prod(result_list)


if __name__ == '__main__':
    tmp_list = read_file_day6("day7.txt")
    print(tmp_list)
    result_list = day_6(tmp_list)
    # # # p1
    print("P1")
    print(result_list)
