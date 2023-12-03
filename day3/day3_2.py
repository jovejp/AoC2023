from func_utils import read_file_array_of_array
from collections import defaultdict


def day3_2(main_list):
    my_sum_list = defaultdict(list)
    row_size = len(main_list)
    col_size = len(main_list[0])
    star_set = set()
    for line_index, line_data in enumerate(main_list):
        str_num = ""
        start_col = 0
        flag = 0
        for col_index, col_data in enumerate(line_data):
            if col_data == "." or not col_data.isdigit() or col_index == len(line_data) - 1:
                if col_data.isdigit():
                    str_num = str_num + col_data
                if str_num != "":
                    for col_chk in [start_col, col_index]:  # current row
                        if 0 <= col_chk < col_size and main_list[line_index][col_chk] == "*":
                            star_set.add((line_index, col_chk))
                            # print(line_index, col_chk, str_num)
                            flag = 1
                    for row_chk in [-1, 1]:  # previous row and next row
                        for col_chk in range(start_col, col_index + 1):
                            if (0 <= line_index + row_chk < row_size and 0 <= col_chk < col_size
                                    and main_list[line_index + row_chk][col_chk] == "*"):
                                star_set.add((line_index + row_chk, col_chk))
                                # print(line_index + row_chk, col_chk, str_num)
                                flag = 1
                    if flag == 1:
                        for star in star_set:
                            my_sum_list[star].append(int(str_num))
                    star_set = set()
                    str_num = ""
                    flag = 0
                start_col = col_index
            elif col_data.isdigit():
                str_num = str_num + col_data
        result = 0
    for k, v in my_sum_list.items():
        # print(k, v)
        if len(v) == 2:
            result += v[0] * v[1]
    return result


if __name__ == '__main__':
    tmp_list = read_file_array_of_array("day3.txt")
    result_list = day3_2(tmp_list)
    # p2
    print("P2")
    print(result_list)
