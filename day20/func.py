import math

from func_utils import read_file_array
from collections import deque, defaultdict
import re

debug = False
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array(file_name)
input_dict = {}
flips = {}
conj = {}
conj_dict = defaultdict(dict)
untyped = []
p = re.compile('[&%]+')
for x in input_list:
    item = x.split("->")
    if p.match(item[0].strip()):
        i_name = item[0][1:].strip()
        if item[0].strip().startswith("%"):
            flips[i_name] = 0  # off 0 , on 1
        else:
            conj[i_name] = 0
    else:
        i_name = item[0].strip()
        untyped.append(item[0].strip())
    input_dict[i_name] = [nn.strip() for nn in item[1].split(",")]

for k, v in input_dict.items():
    for x in v:
        if x in conj.keys():
            conj_dict[x][k] = 0


def func(cycle):
    process = deque()
    f_total = 0
    t_total = 0
    i = 1
    while i <= cycle:
        # start from broadcaster
        process.append(["broadcaster", 0] + input_dict["broadcaster"])
        f_total += 1
        while process:
            next_step = process.popleft()
            for idx in range(2, len(next_step)):
                if next_step[idx] in flips.keys():
                    if next_step[1] == 1:
                        t_total += 1
                        continue
                    else:
                        f_total += 1
                        flips[next_step[idx]] = 1 ^ flips[next_step[idx]]
                        process.append([next_step[idx], flips[next_step[idx]]] + input_dict[next_step[idx]])
                elif next_step[idx] in conj.keys():
                    if next_step[1] == 1:
                        t_total += 1
                        conj_dict[next_step[idx]][next_step[0]] = 1
                    else:
                        f_total += 1
                        conj_dict[next_step[idx]][next_step[0]] = 0
                    conj[next_step[idx]] = 0 if all(vv == 1 for vv in conj_dict[next_step[idx]].values()) else 1
                    process.append([next_step[idx], conj[next_step[idx]]] + input_dict[next_step[idx]])
                elif next_step[idx] in untyped:
                    if next_step[1] == 1:
                        t_total += 1
                    else:
                        f_total += 1
                    process.append([next_step[idx], next_step[1]] + input_dict[next_step[idx]])
                else:
                    if next_step[1] == 1:
                        t_total += 1
                    else:
                        f_total += 1
        i += 1
    return f_total * t_total


def part1():
    result = func(1000)
    return result


def func_part2():
    check_list = defaultdict(list)
    for xx in conj_dict["kz"].keys():
        for xy in conj_dict[xx].keys():
            check_list[xy].append(0)
    process = deque()
    i = 1
    while i < 10000:
        # start from broadcaster
        process.append(["broadcaster", 0] + input_dict["broadcaster"])
        while process:
            next_step = process.popleft()
            for idx in range(2, len(next_step)):
                if next_step[idx] in flips.keys():
                    if next_step[1] == 1:
                        continue
                    else:
                        flips[next_step[idx]] = 1 ^ flips[next_step[idx]]
                        process.append([next_step[idx], flips[next_step[idx]]] + input_dict[next_step[idx]])
                elif next_step[idx] in conj.keys():
                    if next_step[1] == 1:
                        conj_dict[next_step[idx]][next_step[0]] = 1
                    else:
                        conj_dict[next_step[idx]][next_step[0]] = 0
                    conj[next_step[idx]] = 0 if all(vv == 1 for vv in conj_dict[next_step[idx]].values()) else 1
                    if next_step[idx] in check_list.keys() and conj[next_step[idx]] == 0:
                        check_list[next_step[idx]].append(i)
                    if all(len(vv) == 3 for vv in check_list.values()):
                        lcm_list = []
                        for kk, vv in check_list.items():
                            lcm_list.append(vv[-1]-vv[-2])
                        return math.lcm(*lcm_list)
                    process.append([next_step[idx], conj[next_step[idx]]] + input_dict[next_step[idx]])
                elif next_step[idx] in untyped:
                    if next_step[1] == 0:
                        process.append([next_step[idx], next_step[1]] + input_dict[next_step[idx]])
                else:
                    if next_step[1] == 0:
                        print(next_step[1])
                        return i
        i += 1


def part2():
    result = func_part2()
    return result


if __name__ == '__main__':
    r_p1 = part1()
    print("part1", r_p1)
    r_p2 = part2()
    print("part2", r_p2)


