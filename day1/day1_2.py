from func_utils import read_file_array


def day1_2(main_list):
    my_sum_list = []
    replace_list = [("one", 1), ("two", 2), ("three", 3),("four", 4), ("five", 5), ("six", 6),("seven", 7), ("eight", 8), ("nine", 9)]
    for line_data in main_list:
        local_list = []
        min_index = len(line_data)
        min_num = -1
        max_index = -1
        max_num = -1
        for rep_str in replace_list:
            m_index = line_data.find(rep_str[0])
            if m_index != -1 and m_index < min_index:
                min_index = m_index
                min_num = rep_str[1]
            m_index = line_data.rfind(rep_str[0])
            if m_index != -1 and m_index > max_index:
                max_index = m_index
                max_num = rep_str[1]
        print("min_index:", min_index, "min_num:", min_num)
        print("max_index:", max_index, "max_num:", max_num)
        count = 0
        for i in line_data:
            if count == min_index:
                local_list.append(int(min_num))
            if count == max_index:
                local_list.append(int(max_num))
            if i.isdigit():
                local_list.append(int(i))
            count = count + 1
        print(local_list)
        item = local_list[0] * 10 + local_list[-1]
        print(item)
        my_sum_list.append(local_list[0] * 10 + local_list[-1])
    # my_sum_list.sort(key=None, reverse=True)
    return sum(my_sum_list)


if __name__ == '__main__':
    tmp_list = read_file_array("day1_2.txt")
    result_list = day1_2(tmp_list)
    # p2
    print("P2")
    print(result_list)
