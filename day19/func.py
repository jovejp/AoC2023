from func_utils import read_file_arrays
import re
from collections import deque

debug = False
file_name = "input_sample.txt" if debug else "input.txt"
input_list = read_file_arrays(file_name)

workflows = {}
for x in input_list[0]:
    items = re.split('{|}', x)
    wks = items[1].split(",")
    dict_wks = []
    for y in range(len(wks) - 1):
        item = re.split('>|<|:', wks[y])
        dict_wks.append([item[0]] + [wks[y][len(item[0])]] + item[1:])
    dict_wks.append(["Final", wks[-1]])
    workflows[items[0]] = dict_wks

range_q = deque()


def func(dict_rr):
    wf = "in"
    while wf:
        if wf in ["A", "R"]:
            return wf
        cur_wf = workflows[wf]
        for v in cur_wf:
            if v[0] == "Final":
                wf = v[1]
                break
            elif v[1] == "<":
                if dict_rr[v[0]] < int(v[2]):
                    wf = v[3]
                    break
                else:
                    continue
            elif v[1] == ">":
                if dict_rr[v[0]] > int(v[2]):
                    wf = v[3]
                    break
                else:
                    continue
            else:
                print("error!!!", v[0], "is not correct")


def part1():
    result = 0
    for row_data in input_list[1]:
        row_data = row_data.replace("{", "").replace("}", "")
        rr = row_data.split(",")
        dict_rr = {}
        for cc in rr:
            ii = cc.split("=")
            dict_rr[ii[0]] = int(ii[1])
        if func(dict_rr) == "A":
            result += sum(dict_rr.values())
    return result


def func_part2():
    processed_list = []
    while range_q:
        cur_range = range_q.pop()
        if cur_range[0] in ["A", "R"]:
            processed_list.append(cur_range)
            continue
        cur_wf = workflows[cur_range[0]]
        cur_data = cur_range[1].copy()
        # print(cur_range)
        for v in cur_wf:
            if v[0] == "Final":
                range_q.append([v[1], cur_data])
                break
            elif v[1] == "<":
                v_data = int(v[2])
                if cur_data[v[0]][0] < v_data < cur_data[v[0]][1]:
                    next_data_i = cur_data.copy()
                    next_data_i[v[0]] = [cur_data[v[0]][0], v_data - 1]
                    range_q.append([v[3], next_data_i])
                    cur_data[v[0]] = [v_data, cur_data[v[0]][1]]
                    continue
                elif cur_data[v[0]][0] >= v_data:
                    continue
                elif cur_data[v[0]][1] < v_data:
                    range_q.append([v[3], cur_data])
                    break
            elif v[1] == ">":
                v_data = int(v[2])
                if cur_data[v[0]][0] < v_data < cur_data[v[0]][1]:
                    next_data_a = cur_data.copy()
                    next_data_a[v[0]] = [v_data + 1, cur_data[v[0]][1]]
                    range_q.append([v[3], next_data_a])
                    cur_data[v[0]] = [cur_data[v[0]][0], v_data]
                    continue
                elif cur_data[v[0]][0] > v_data:
                    range_q.append([v[3], cur_data])
                    break
                elif cur_data[v[0]][1] <= v_data:
                    continue
            else:
                print("error!!!", v[0], "is not correct")

    return processed_list

def part2():
    result = 0
    range_q.append(["in", {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}])
    processed_list = func_part2()
    for ii in processed_list:
        if ii[0] == "A":
            xx = ii[1]
            result += ((xx['x'][1] - xx['x'][0] + 1) * (xx['m'][1] - xx['m'][0] + 1)
                       * (xx['a'][1] - xx['a'][0] + 1) * (xx['s'][1] - xx['s'][0] + 1))
    return result


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
    r_p2 = part2()
    print("part2", r_p2)
