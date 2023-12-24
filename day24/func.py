from func_utils import read_file_array
import itertools

debug = False
file_name = "input_sample.txt" if debug else "input.txt"
# mn = 7
# mm = 27
mn = 200000000000000
mm = 400000000000000
input_list = read_file_array(file_name)
ns = [[int(y.strip()) for x in row_data.split("@") for y in x.strip().split(",")] for row_data in input_list]
ns_box = {}
for xx in ns:
    board_point = []
    key = tuple(xx[:3])
    ns_box[key] = []
    for nn in [mn, mm]:
        step1 = (nn - xx[0]) / xx[3]
        if step1 > 0 and mn <= xx[0] + xx[3] * step1 <= mm and mn <= xx[1] + xx[4] * step1 <= mm:
            ns_box[key].append((xx[0] + xx[3] * step1, xx[1] + xx[4] * step1))
        step2 = (nn - xx[1]) / xx[4]
        if step2 > 0 and mn <= xx[0] + xx[3] * step2 <= mm and mn <= xx[1] + xx[4] * step2 <= mm:
            ns_box[key].append((xx[0] + xx[3] * step2, xx[1] + xx[4] * step2))

    if len(ns_box[key]) > 2:
        print("error!!!!", xx)
    elif len(ns_box[key]) == 1:
        if mn <= xx[0] <= mm and mn <= xx[1] <= mm:
            ns_box[key].append((xx[0], xx[1]))
        else:
            print("error!!!!", xx)
    elif len(ns_box[key]) == 0:
        # print(ns_box[key], "pass points", xx, )
        del ns_box[key]
total_rows = len(ns_box)


def quick_check(a, b):
    (a1x, a1y), (a2x, a2y) = ns_box[a]
    (b1x, b1y), (b2x, b2y) = ns_box[b]
    if (max(a1x, a2x) < min(b1x, b2x) or max(b1x, b2x) < min(a1x, a2x)
            or max(a1y, a2y) < min(b1y, b2y) or max(b1y, b2y) < min(a1y, a2y)):
        return False
    else:
        return True


def cell_vector(a, b, c, d):
    return (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])


def final_check(x, y):
    a, b = ns_box[x]
    c, d = ns_box[y]
    return True if (cell_vector(c, d, c, a) * cell_vector(c, d, c, b) < 0
                    and cell_vector(a, b, a, c) * cell_vector(a, b, a, d) < 0) else False


def func():
    count = 0
    for a, b in itertools.combinations(ns_box, 2):
        count += (1 if final_check(a, b) else 0) if quick_check(a, b) else 0
    return count


def part1():
    result = func()
    return result


def part2():
    result = func()
    return result


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
#     r_p2 = part2()
#     print("part2", r_p2)
