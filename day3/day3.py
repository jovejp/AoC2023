from func_utils import read_file_array_of_array


def day_3(main_list):
    my_sum_list = []
    row_size = len(main_list)
    col_size = len(main_list[0])
    for line_index, line_data in enumerate(main_list):
        str_num = ""
        start_col = 0
        flag = 0
        for col_index, col_data in enumerate(line_data):
            if col_data == "." or not col_data.isdigit() or col_index == len(line_data) - 1:
                if col_data.isdigit():
                    str_num = str_num + col_data
                if str_num != "":
                    for col_chk in [start_col, col_index]:
                        if (0 <= col_chk < col_size and main_list[line_index][col_chk] != "."
                                and not main_list[line_index][col_chk].isdigit()):
                            flag = 1
                            break
                    for row_chk in [-1, 1]:
                        for col_chk in range(start_col, col_index + 1):
                            if (0 <= line_index + row_chk < row_size and 0 <= col_chk < col_size
                                    and main_list[line_index + row_chk][col_chk] != "."
                                    and not main_list[line_index + row_chk][col_chk].isdigit()):
                                flag = 1
                                break
                    if flag == 1:
                        my_sum_list.append(int(str_num))
                    str_num = ""
                    flag = 0
                start_col = col_index
            elif col_data.isdigit():
                str_num = str_num + col_data
    return sum(my_sum_list)


if __name__ == '__main__':
    tmp_list = read_file_array_of_array("day3.txt")
    result_list = day_3(tmp_list)
    # p1
    print("P1")
    print(result_list)
