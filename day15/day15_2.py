from collections import defaultdict

input_list = open("day15.txt").readline().strip().split(",")
total_rows = len(input_list)
box_full = defaultdict(defaultdict)


def get_hash(item):
    cur = 0
    for x in item:
        cur = (cur + ord(x)) * 17 % 256
    return cur


def process_box(item):
    if "=" in item:
        key, value = item.split("=")
        box = get_hash(key)
        box_full[box][key] = value
    elif "-" in item:
        key, value = item.split("-")
        box = get_hash(key)
        if key in box_full[box].keys():
            del box_full[box][key]
    else:
        print("error!!!!", item)


def day_15(data):
    total = 0
    for x in data:
        process_box(x)
    for k, v in box_full.items():
        # print(k, v)
        step = 0
        for idy, y in enumerate(box_full[k].values()):
            step += (k+1) * (idy+1) * int(y)
        # print(k, step)
        total += step
    return total


if __name__ == '__main__':
    total_step = day_15(input_list)
    print(total_step)
