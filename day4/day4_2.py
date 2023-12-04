from func_utils import read_file_array
from collections import defaultdict


def day4_2(main_list):
    my_sum_list = defaultdict(int)
    for line_index, line_data in enumerate(main_list):
        my_sum_list[line_index] += 1
        card_data = line_data.split(":")[1]
        win_cards, my_cards = card_data.split("|")
        win_cards = win_cards.split()
        my_cards = my_cards.split()
        common_card_size = (len(set(win_cards) & set(my_cards)))
        if common_card_size > 0:
            # print(line_index, common_card_size)
            for i in range(common_card_size):
                my_sum_list[line_index + 1 + i] += my_sum_list[line_index]

    return sum(my_sum_list.values())


if __name__ == '__main__':
    tmp_list = read_file_array("day4.txt")
    result_list = day4_2(tmp_list)
    # p1
    print("P2")
    print(result_list)
