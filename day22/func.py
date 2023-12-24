from func_utils import read_file_array
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from copy import deepcopy

debug = False
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


# def dfs(key):
#     worker_q = deque([key])
#     push_later_set = set()
#     next_push_later_set = set()
#     result = []
#     while worker_q or push_later_set:
#         if not worker_q :
#             # for the brick depends on multiple bricks, check if all depends on bricks be impacted.
#             if push_later_set:
#                 while push_later_set:
#                     if_node = push_later_set.pop()
#                     if all(rr in result + [cur_node] for rr in ls_depends_on[if_node]):
#                         if if_node not in result:
#                             print(if_node, "vv in critical")
#                             result.append(if_node)
#                             worker_q.append(if_node)
#                     else:
#                         next_push_later_set.add(if_node)
#                 push_later_set = next_push_later_set.copy()
#                 next_push_later_set.clear()
#                 if worker_q:
#                     continue
#                 else:
#                     break
#         cur_node = worker_q.pop()
#         if len(ls_depends_by[cur_node]) > 0:
#             for vv in ls_depends_by[cur_node]:
#                 if all(rr in result + [cur_node] for rr in ls_depends_on[vv]):
#                     if vv not in result:
#                         result.append(vv)
#                         worker_q.append(vv)
#                 else:
#                     if vv not in push_later_set:
#                         push_later_set.add(vv)
#     return result

def dfs(key):
    worker_q = deque([key])
    result = []
    while worker_q:
        cur_node = worker_q.pop()
        if len(ls_depends_by[cur_node]) > 0:
            for vv in ls_depends_by[cur_node]:
                if all(rr in result + [cur_node] for rr in ls_depends_on[vv]):
                    if vv not in result:
                        result.append(vv)
                        worker_q.append(vv)
    return result


def func_part2(ls_puzzle):
    total = 0
    rev_ls_puzzle = deepcopy(ls_puzzle)
    rev_ls_puzzle = OrderedDict(
        sorted(rev_ls_puzzle.items(), key=lambda item: (item[1][0], item[0][0], item[0][1]), reverse=True))
    for key in rev_ls_puzzle.keys():
        if key not in movable_bricks:
            value = set(dfs(key))
            total += len(value)
    return total


def part2(ls_puzzle):
    result = func_part2(ls_puzzle)
    return result


if __name__ == '__main__':
    ls_tower = process_input()
    ls_o_tower = fall(ls_tower)
    ls_b_tower = deepcopy(ls_o_tower)
    depends(ls_o_tower)
    r_p1 = part1(ls_o_tower)
    print("part1", r_p1)

    r_p2 = part2(ls_b_tower)
    print("part2", r_p2)
