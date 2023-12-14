from func_utils import read_file_array_of_array

input_list = read_file_array_of_array("day14.txt")
total_rows = len(input_list)
total_cols = len(input_list[0])
print("total_rows", total_rows)
print("total_cols", total_cols)


def move_one_step(data):
    row = 0
    while row < total_rows - 1:
        col = 0
        while col < total_cols:
            if data[row][col] == "." and data[row + 1][col] == "O":
                data[row][col] = "O"
                data[row + 1][col] = "."
            col += 1
        row += 1
    return data


def day_14(data):
    total = 0
    row = 1
    while row < total_rows - 1:
        move_one_step(data)
        # for x in data:
        #     print(row, x)
        row += 1

    for idx, x in enumerate(data):
        # print(idx, x)
        total = total + (total_rows - idx) * x.count("O")
    return total


if __name__ == '__main__':
    total_step = day_14(input_list)
    print(total_step)
