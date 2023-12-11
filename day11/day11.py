from func_utils import read_file_array_of_array
from collections import defaultdict

input_list = read_file_array_of_array("day11.txt")
col_size = len(input_list[0])
row_size = len(input_list)

# print(col_size, row_size)


def day_10(data):
    # find star row and cols
    star_row_dict = defaultdict(list)
    star_col_dict = defaultdict(list)

    for idx, x in enumerate(input_list):
        for idy, y in enumerate(x):
            if y == "#":
                star_row_dict[idx].append(idy)
                star_col_dict[idy].append(idx)

    # create pairs and generate steps
    node_list = []
    for k, v in star_row_dict.items():
        for d in v:
            node_list.append([k, d])
    node_list = sorted(node_list, key=lambda kx: (kx[0], kx[1]), reverse=True)

    total_steps = 0
    count_pairs = 0
    while len(node_list) > 1:
        item = node_list.pop()
        for x in node_list:
            count_pairs += 1

            nx = item[0]
            ny = min(item[1], x[1])
            gapx = 0
            gapy = 0
            while item[0] <= nx <= x[0]:
                if nx not in star_row_dict.keys():
                    gapx = gapx + 1
                nx += 1
            while min(item[1], x[1]) <= ny <= max(item[1],x[1]):
                if ny not in star_col_dict.keys():
                    gapy = gapy + 1
                ny += 1
            steps = x[0] - item[0] +  gapx + abs(x[1] - item[1]) + gapy
            print(count_pairs, "pair", item, "with", x, steps)
            total_steps += steps
    return total_steps


if __name__ == '__main__':
    total_step = day_10(input_list)
    print(total_step)
