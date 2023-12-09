from func_utils import read_file_array


def find_gap(data):
    result = []
    for i in range(len(data)-1):
        result.append(data[i+1] - data[i])
    if all(x == 0 for x in result):
        return 0
    else:
        return result[-1] + find_gap(result)


def day_9(data):
    result = 0
    for item in data:
        line_data = [int(x) for x in item.split()]
        result = result + line_data[-1] + find_gap(line_data)
    return result


if __name__ == '__main__':
    input_list = read_file_array("day9.txt")
    total_step = day_9(input_list)
    print(total_step)
