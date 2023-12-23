from func_utils import read_file_array
from collections import OrderedDict
from collections import defaultdict
from copy import deepcopy

debug = True
file_name = "input_sample.txt" if debug else "input.txt"
input_list = read_file_array(file_name)


def process_input():
    ls_puzzle = {}
    for rdx, rr in enumerate(input_list):
        cur_item = rr.split("~")
        n1, n2 = [(int(x1)) for x1 in cur_item[0].split(",")], [int(x2) for x2 in cur_item[1].split(",")]
        ls_puzzle[(n1[2], rdx)] = [n1[2], n2[2] - n1[2]]
        if n1[0] == n2[0]:
            for ncc in range(min(n1[1], n2[1]), max(n1[1], n2[1]) + 1):
                ls_puzzle[(n1[2], rdx)].append((n1[0], ncc))
        elif n1[1] == n2[1]:
            for nrr in range(min(n1[0], n2[0]), max(n1[0], n2[0]) + 1):
                ls_puzzle[(n1[2], rdx)].append((nrr, n1[1]))
        else:
            print("input data special case, checking!!!", n1, n2)
    return OrderedDict(sorted(ls_puzzle.items(), key=lambda item: (item[1][0], item[0][0], item[0][1])))


ls_moved_bricks = defaultdict(list)  # bricks in each floor after moved


def fall(ls_puzzle):
    ls_moved_tower = defaultdict(list)
    for k, v in ls_puzzle.items():
        if v[0] == 1:
            ls_moved_tower[v[0]] += v[2:]
            ls_moved_bricks[v[0]] += [k]
        else:
            cdx = v[0] - 1
            while cdx >= 0:
                if any(vv in ls_moved_tower[cdx] for vv in v[2:]) or cdx == 0:
                    ls_puzzle[k][0] = cdx + 1
                    for yy in range(v[1] + 1):
                        ls_moved_tower[cdx + yy + 1] += [vv for vv in v[2:] if vv not in ls_moved_tower[cdx + yy + 1]]
                        ls_moved_bricks[cdx + yy + 1] += [k]
                    break
                else:
                    cdx -= 1
    return OrderedDict(sorted(ls_puzzle.items(), key=lambda item: (item[1][0], item[0][0], item[0][1])))


ls_depends_on = defaultdict(list)
ls_depends_by = defaultdict(list)


def depends(ls_puzzle):
    for kk, vv in ls_puzzle.items():
        for pkk in ls_moved_bricks[vv[0] - 1]:
            if any(vvv in ls_puzzle[pkk][2:] for vvv in vv[2:]):
                ls_depends_on[kk].append(pkk)
                ls_depends_by[pkk].append(kk)


movable_bricks = set()


def func(ls_puzzle):
    depends(ls_puzzle)
    not_movable_bricks = set()
    for key in ls_puzzle.keys():
        if len(ls_depends_on[key]) == 1:
            if ls_depends_on[key][0] not in not_movable_bricks:
                not_movable_bricks.add(ls_depends_on[key][0])

    for key in ls_puzzle.keys():
        if len(ls_depends_on[key]) >= 2:
            for vvv in ls_depends_on[key]:
                if vvv not in movable_bricks and vvv not in not_movable_bricks:
                    movable_bricks.add(vvv)
        elif len(ls_depends_on[key]) == 0:
            if key not in movable_bricks and key not in not_movable_bricks:
                movable_bricks.add(key)
        if key not in ls_depends_by.keys():
            if key not in movable_bricks and key not in not_movable_bricks:
                movable_bricks.add(key)


def part1(ls_puzzle):
    func(ls_puzzle)
    return len(movable_bricks)


result_list = defaultdict(list)


def dfs(key, processed_nodes):
    # print("dfs started", key, processed_nodes)
    if key in result_list.keys():
        return result_list[key]
    result = []
    next_list = []
    all_next_valid_flag = True
    if len(ls_depends_by[key]) > 0:
        for vv in ls_depends_by[key]:
            if all(rr in processed_nodes + [key] for rr in ls_depends_on[vv]):
                if vv not in result:
                    result += [vv]
                    next_list.append(vv)
            # else:
                # print("which action need???", key, ls_depends_by[key], vv, ls_depends_on[vv], processed_nodes)
        for vv in next_list:
            # print("dfs -callback", key, vv, next_list, "by", ls_depends_by[key], "on", ls_depends_on[vv])
            result = list(set(result + dfs(vv, list(set(processed_nodes + result)))))
    # else:
        # print("!!!!", key, "no depend by", ls_depends_by[key])
    if (len(ls_depends_by[key]) == 1 and len(ls_depends_on[ls_depends_by[key][0]]) == 1 and
            key == ls_depends_on[ls_depends_by[key][0]][0] and processed_nodes == []):
        # print("******memory", key, list(set(result)), 'refer info', ls_depends_by[key], ls_depends_on[ls_depends_by[key][0]][0])
        result_list[key] = list(set(result))
    # print("final****=====", key, list(set(result)))
    return result


def func_part2(ls_puzzle):
    total = 0
    rev_ls_puzzle = deepcopy(ls_puzzle)
    rev_ls_puzzle = OrderedDict(
        sorted(rev_ls_puzzle.items(), key=lambda item: (item[1][0], item[0][0], item[0][1]), reverse=True))
    # func(ls_puzzle)
    print(ls_depends_by)
    for key in rev_ls_puzzle.keys():
        if key not in movable_bricks:
            value = set(dfs(key, []))
            # print(key, len(value), value)
            total += len(value)
    return total


def part2(ls_puzzle):
    result = func_part2(ls_puzzle)
    return result


if __name__ == '__main__':
    ls_tower = process_input()
    ls_o_tower = fall(ls_tower)
    ls_b_tower = deepcopy(ls_o_tower)
    r_p1 = part1(ls_o_tower)
    print("part1", r_p1)

    r_p2 = part2(ls_b_tower)
    print("part2", r_p2)
