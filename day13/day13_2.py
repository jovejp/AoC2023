from func_utils import read_file_arrays

input_list = read_file_arrays("day13.txt")


def search_mirror(data_idx, data):
    total_rows = len(data)
    total_cols = len(data[0])
    print(data_idx, "check cols")
    mirror = 0
    idx = 1
    while idx < total_cols:
        if idx <= total_cols / 2:
            minx = 0
            maxy = 2 * idx
        else:
            minx = 2 * idx - total_cols
            maxy = total_cols
        chk_flag = True
        allow_wrong = 1
        for x in data:
            # print(x, minx, idx, maxy)
            # print(x[minx:idx][::-1], x[idx: maxy])
            if x[minx:idx][::-1] != x[idx: maxy] and allow_wrong == 1:
                if len([(x + y).replace(y, "")
                        for x, y in zip(x[minx:idx][::-1], x[idx: maxy])
                        if (x + y).replace(y, "") != '']) == 1:
                    allow_wrong = 0
                else:
                    chk_flag = False
                    break
            elif x[minx:idx][::-1] != x[idx: maxy] and allow_wrong == 0:
                chk_flag = False
                break
        if chk_flag and allow_wrong == 0:
            mirror = idx
            break
        idx += 1
    if mirror > 0:
        return mirror

    # rows
    print(data_idx, "check rows")
    idy = 1
    while idy < total_rows:
        allow_wrong = 1
        chk_flag = True
        i = 1
        while 0 <= idy - i < idy + i - 1 < total_rows:
            if data[idy + i - 1] != data[idy - i] and allow_wrong == 1:
                if len([(x + y).replace(y, "")
                        for x, y in zip(data[idy + i - 1], data[idy - i])
                        if (x + y).replace(y, "") != '']) == 1:
                    allow_wrong = 0
                else:
                    chk_flag = False
                    break
            elif data[idy + i - 1] != data[idy - i] and allow_wrong == 0:
                chk_flag = False
                break
            i += 1
        if chk_flag and allow_wrong == 0:
            mirror += idy * 100
            break
        idy += 1
    return mirror


def day_13(data):
    total = 0
    for idx, x in enumerate(data):
        mirror = search_mirror(idx, x)
        if mirror == 0:
            print("Error!!!!")
        total += mirror
    return total


if __name__ == '__main__':
    total_step = day_13(input_list)
    print(total_step)
