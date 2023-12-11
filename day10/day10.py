from func_utils import read_file_array_of_array
from collections import defaultdict

input_list = read_file_array_of_array("day10.txt")
col_size = len(input_list[0])
row_size = len(input_list)
moved_step = []
valid_next_step = defaultdict(list)
pipelines = ["J", "7", "F", "-", "L", "|"]


def day_10(data):
    # find start point
    sx, sy = 0, 0
    for idx, item in enumerate(data):
        if "S" in item:
            sx = idx
            sy = item.index("S")
            break
    steps_list = []
    # move and check step
    for pipeline in pipelines:
        step = 0
        process_list = []
        moved_list = []
        process_list.append([sx, sy])
        print("start check", pipeline)
        while process_list:
            nx, ny = process_list.pop()
            if [nx, ny] in moved_list:
                # print("final", nx, ny, moved_list)
                steps_list.append(step / 2)
                break
            else:
                step += 1
                moved_list.append([nx, ny])
                cur_pipe = pipeline if [sx, sy] == [nx, ny] else data[nx][ny]
                if ny - 1 >= 0:
                    next_l = data[nx][ny - 1]
                    if next_l != ".":
                        if (cur_pipe in ["-", "7", "J"] and next_l in ["-", "F", "L"]
                                and ([nx, ny - 1] not in moved_list)):
                            process_list.append([nx, ny - 1])
                if ny + 1 < col_size:
                    next_r = data[nx][ny + 1]
                    if next_r != ".":
                        if (cur_pipe in ["-", "L", "F"] and next_r in ["-", "7", "J"]
                                and ([nx, ny + 1] not in moved_list)):
                            process_list.append([nx, ny + 1])
                if nx - 1 >= 0:
                    next_t = data[nx - 1][ny]
                    if next_t != ".":
                        if (cur_pipe in ["|", "L", "J"] and next_t in ["F", "7", "|"]
                                and ([nx - 1, ny] not in moved_list)):
                            process_list.append([nx - 1, ny])
                if nx + 1 < row_size:
                    next_b = data[nx + 1][ny]
                    if next_b != ".":
                        if (cur_pipe in ["|", "F", "7"] and next_b in ["L", "J", "|"]
                                and ([nx + 1, ny] not in moved_list)):
                            process_list.append([nx + 1, ny])
                # print("next", step, cur_pipe, process_list)
        print("checked", pipeline)
        if steps_list:
            break
    return steps_list


if __name__ == '__main__':
    input_list = read_file_array_of_array("day10.txt")
    total_step = day_10(input_list)
    print(total_step)
