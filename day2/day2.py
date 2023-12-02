from func_utils import read_file_array


def day_2(main_list):
    my_sum_list = []
    check_list = {"red": 12, "green": 13, "blue": 14}
    for line_data in main_list:
        game_no = line_data.split(":")[0].split()[1]
        items = line_data.split(":")[1].split(";")
        flag = 0
        for item in items:
            for sub_item in item.split(","):
                num, color = sub_item.split()
                if int(num) > check_list.get(color):
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            my_sum_list.append(int(game_no))
    return sum(my_sum_list)


if __name__ == '__main__':
    tmp_list = read_file_array("day2.txt")
    result_list = day_2(tmp_list)
    # p1
    print("P1")
    print(result_list)
