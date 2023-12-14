

import numpy as np
from func_utils import read_file_array_of_array

input_list = read_file_array_of_array("day14.txt")
total_rows = len(input_list)
total_cols = len(input_list[0])
print("total_rows", total_rows)
print("total_cols", total_cols)


def move_cycle(data):
    # print("move up")
    # move up
    prev_data = data.copy()
    step = 0
    while step < total_rows:
        row = 0
        while row < total_rows - 1:
            col = 0
            while col < total_cols:
                if data[row][col] == "." and data[row + 1][col] == "O":
                    data[row][col] = "O"
                    data[row + 1][col] = "."
                col += 1
            row += 1
        if (prev_data == data).all():
            break
        else:
            prev_data = data.copy()
        step += 1
    # print("move left")
    # move left
    step = 0
    while step < total_cols:
        col = 0
        while col < total_cols - 1:
            row = 0
            while row < total_rows:
                if data[row][col] == "." and data[row][col + 1] == "O":
                    data[row][col] = "O"
                    data[row][col + 1] = "."
                row += 1
            col += 1
        if (prev_data == data).all():
            break
        else:
            prev_data = data.copy()
        step += 1
    # print("move down")
    # move down
    step = 0
    while step < total_rows:
        row = total_rows - 1
        while row > 0:
            col = 0
            while col < total_cols:
                if data[row][col] == "." and data[row - 1][col] == "O":
                    data[row][col] = "O"
                    data[row - 1][col] = "."
                col += 1
            row -= 1
        if (prev_data == data).all():
            break
        else:
            prev_data = data.copy()
        step += 1
    # print("move right")
    # move right
    step = 0
    while step < total_cols:
        col = total_cols - 1
        while col > 0:
            row = 0
            while row < total_rows:
                if data[row][col] == "." and data[row][col - 1] == "O":
                    data[row][col] = "O"
                    data[row][col - 1] = "."
                row += 1
            col -= 1
        if (prev_data == data).all():
            print(row, col)
            break
        else:
            prev_data = data.copy()
        step += 1


def day_14(data):
    total = 0
    total_times = 1000000000
    time = 1
    data = np.array(data)
    prev_data_list = {}
    while time <= total_times:
        move_cycle(data)
        key = tuple(tuple(x) for x in data)
        if key in prev_data_list:
            print("find one time!!!", time, prev_data_list[key], time - prev_data_list[key])
            time = total_times - ((total_times - time) % (time - prev_data_list[key]))
        else:
            prev_data_list[key] = time
            print("loop one time:", time)
        time += 1

    for idx, x in enumerate(data):
        total = total + (total_rows - idx) * (x == "O").sum()
    return total


if __name__ == '__main__':
    total_step = day_14(input_list)
    print(total_step)
