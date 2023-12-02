from func_utils import read_file_array
from collections import defaultdict
import numpy


def day2_2(main_list):
    my_sum_list = []
    for line_data in main_list:
        max_color = defaultdict(int)
        items = line_data.split(":")[1].split(";")
        for item in items:
            for sub_item in item.split(","):
                num, color = sub_item.split()
                max_color[color] = max(max_color[color], int(num))
        my_sum_list.append(numpy.prod(list(max_color.values())))
    return sum(my_sum_list)


if __name__ == '__main__':
    tmp_list = read_file_array("day2.txt")
    result_list = day2_2(tmp_list)
    # p2
    print("P2")
    print(result_list)
