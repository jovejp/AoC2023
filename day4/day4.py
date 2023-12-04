from func_utils import read_file_array


def day_4(main_list):
    my_sum_list = []
    for line_index, line_data in enumerate(main_list):
        card_data = line_data.split(":")[1]
        win_cards, my_cards = card_data.split("|")
        win_cards = win_cards.split()
        my_cards = my_cards.split()
        common_card_size = (len(set(win_cards) & set(my_cards)))
        print(line_index, common_card_size)
        if common_card_size > 0:
            my_sum_list.append(int(2**(common_card_size-1)))
    return sum(my_sum_list)


if __name__ == '__main__':
    tmp_list = read_file_array("day4.txt")
    result_list = day_4(tmp_list)
    # p1
    print("P1")
    print(result_list)
