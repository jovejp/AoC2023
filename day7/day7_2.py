def find_type(data):
    check_list = []
    y = 0
    yx = 0
    for x in data:
        if x != "J":
            check_list.append(data.count(x))
    if check_list:
        y = max(check_list)
    if y == 1:
        if data.count("J") > 0:
            yx = 0
    elif y == 2:
        yx = int(check_list.count(2) / 2) - 1
    elif y == 3:
        yx = int(check_list.count(2) / 2)
    else:
        yx = 0
    return y + data.count("J"), yx


def rep_str(data):
    src_char = ["A", "K", "Q", "J", "T"]
    rep_char = ["Z", "Y", "X", "1", "V"]
    for i, d in enumerate(src_char):
        data = data.replace(d, rep_char[i])
    return data


def read_file_day7(file_name):
    line_data = []
    f = open(file_name)
    line = f.readline()
    while line:
        row_data = line.split()
        y, yx = find_type(row_data[0])
        line_data.append([rep_str(row_data[0]), y, yx, int(row_data[1]), row_data[0]])
        line = f.readline()
    f.close()
    # print(line_data)
    line_data = sorted(line_data, key=lambda x: (x[1], x[2], x[0]))
    return line_data


def day_7(main_list):
    return_result = 0
    for index, data in enumerate(main_list):
        return_result += (index + 1) * data[3]
    return return_result


if __name__ == '__main__':
    tmp_list = read_file_day7("day7.txt")
    # print(tmp_list)
    result_list = day_7(tmp_list)
    print(result_list)
