from collections import defaultdict


def read_file_day6(file_name):
    line_data = defaultdict(list)
    f = open(file_name)
    line_data["time"] = int (f.readline().split(":")[1].replace(" ",""))
    line_data["distance"] = int (f.readline().split(":")[1].replace(" ",""))
    f.close()
    return line_data


def day_6(main_list):
    time = main_list["time"]
    dist = main_list["distance"]
    count = 0
    start_num = int(dist / time)
    print(start_num)
    x = start_num
    while x < time:
        # print("x", x, "count", count)
        if x * (time - x) > dist and (x + start_num) * (time - x - start_num) > dist:
            x = x + start_num
            count = count + start_num
        elif x * (time - x) > dist:
            count += 1
            x += 1
        else:
            x += 1
            if count > 0:
                break
    return count


if __name__ == '__main__':
    tmp_list = read_file_day6("day6.txt")
    print(tmp_list)
    result_list = day_6(tmp_list)
    # # # p1
    print("P2")
    print(result_list)
