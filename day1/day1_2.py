from func_utils import read_file_array


def day1_2(main_list):
    my_sum_list = []
    str_num_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line_data in main_list:
        local_list = []
        for i, c in enumerate(line_data):
            if c.isdigit():
                local_list.append(c)
            else:
                for d, v in enumerate(str_num_list):
                    if line_data[i:].startswith(v):
                        local_list.append(str(d + 1))
        item = local_list[0] + local_list[-1]
        # print(item)
        my_sum_list.append(int(local_list[0] + local_list[-1]))
    return sum(my_sum_list)


if __name__ == '__main__':
    tmp_list = read_file_array("day1_2.txt")
    result_list = day1_2(tmp_list)
    # p2
    print("P2")
    print(result_list)
