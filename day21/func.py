from func_utils import read_file_array_of_array

debug = False
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array_of_array(file_name)
total_rows = len(input_list)
total_cols = len(input_list[0])
for idx, x in enumerate(input_list):
    if 'S' in x:
        # print(idx, x.index('S'))
        start_cell = (idx, x.index('S'))
        break
# print("total_rows", total_rows)
# print("total_cols", total_cols)
arrow_pattern = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def func(steps):
    print("plan to process", steps, "steps")
    i = 0
    visited_node = set()
    cur_process = [start_cell]
    next_process = []
    visited_node_his = {}
    while i <= steps:
        visited_node_his[i] = cur_process.copy()
        # print(i, len(visited_node_his[i]), visited_node_his[i])
        while cur_process:
            # print("step", i, "process_node", cur_process)
            cur_node = cur_process.pop()
            visited_node.add(tuple(cur_node))
            for xx in arrow_pattern:
                next_xx, next_yy = cur_node[0] + xx[0], cur_node[1] + xx[1]
                # if (0 <= next_xx < total_rows and 0 <= next_yy < total_cols and input_list[next_xx][next_yy] != "#"
                #         and [next_xx, next_yy] not in next_process and tuple([next_xx, next_yy]) not in visited_node):
                if (input_list[next_xx % total_rows][next_yy % total_cols] != "#"
                        and [next_xx, next_yy] not in next_process
                        and tuple([next_xx, next_yy]) not in visited_node):
                    next_process.append([next_xx, next_yy])
        cur_process = next_process.copy()
        next_process.clear()

        if i % 50 == 0:
            print(i, " rounds detected...")
        i += 1

    results = []
    total_steps_even = 0
    total_steps_odd = 0
    for xx in range(len(visited_node_his)):
        if xx <= steps and xx % 2 == 0:
            total_steps_odd += len(visited_node_his[xx])
        else:
            total_steps_even += len(visited_node_his[xx])
        if xx == 64:
            print('part1', total_steps_odd)
            results.append(total_steps_odd)
        if xx % total_rows == steps % total_rows:
            if xx % 2 == 0:
                results.append(total_steps_odd)
            else:
                results.append(total_steps_even)
            # print("part2", len(results), "xx", xx, xx // total_rows, results[-1])
        if len(results) == 4:
            break
    return results


def func_part2(steps):
    assert total_rows == total_cols
    result = func(2 * total_rows + steps % total_rows)
    v1, v2, v3 = result[1], result[2], result[3]
    a, c = v1 / 2 - v2 + v3 / 2, v1
    b = v2 - v1 - a
    mtimes = steps // total_rows
    return int(a * mtimes * mtimes + b * mtimes + c)


def part2():
    result = func_part2(26501365)
    return result


if __name__ == '__main__':
    r_p2 = part2()
    print("part2", r_p2)
