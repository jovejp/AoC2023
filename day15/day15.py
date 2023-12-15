input_list = open("day15.txt").readline().strip().split(",")
total_rows = len(input_list)
print("total_rows", total_rows)


def get_hash(item):
    cur = 0
    for x in item:
        cur = (cur + ord(x)) * 17 % 256
    return cur


def day_15(data):
    total = 0
    for x in data:
        total += get_hash(x)

    return total


if __name__ == '__main__':
    total_step = day_15(input_list)
    print(total_step)
