from func_utils import read_file_array


def day_1(main_list):
    my_sum_list = []
    for line_data in main_list:
        local_list = []
        for i in line_data:
            if i.isdigit():
                local_list.append(i)
        my_sum_list.append(int(local_list[0] + local_list[-1]))
    return sum(my_sum_list)


if __name__ == '__main__':
    tmp_list = read_file_array("day1.txt")
    result_list = day_1(tmp_list)
    # p1
    print("P1")
    print(result_list)
