from collections import defaultdict
import time


def read_file_day6(file_name):
    line_data = defaultdict(list)
    f = open(file_name)
    line_data["time"] = int(f.readline().split(":")[1].replace(" ", ""))
    line_data["distance"] = int(f.readline().split(":")[1].replace(" ", ""))
    f.close()
    return line_data


def search(nums, time, target, flag):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if flag:
            if nums[mid] * (time - nums[mid]) < target:
                left = mid + 1
            else:
                right = mid
        else:
            if nums[mid] * (time - nums[mid]) > target:
                left = mid + 1
            else:
                right = mid
    # print("find mid", left, nums[left] * (time - nums[left]), target)
    return left


def day6_2_new(main_list):
    game_time = main_list["time"]
    dist = main_list["distance"]
    count = 0
    start_num = int(dist / game_time)
    x = start_num + search(range(start_num, 2 * start_num), game_time, dist, True)
    while x < game_time:
        if x * (game_time - x) > dist:
            if (x + start_num) * (game_time - x - start_num) > dist:
                x = x + start_num
                count = count + start_num
            else:
                y = search(range(x, x + start_num), game_time, dist, False)
                count = count + y
                x = x + y + 1
        else:
            x += 1
            if count > 0:
                break
    return count


def day6_2(main_list):
    game_time = main_list["time"]
    dist = main_list["distance"]
    count = 0
    start_num = int(dist / game_time)
    print(start_num)
    x = start_num
    while x < game_time:
        # print("x", x, "count", count)
        if x * (game_time - x) > dist and (x + start_num) * (game_time - x - start_num) > dist:
            x = x + start_num
            count = count + start_num
        elif x * (game_time - x) > dist:
            count += 1
            x += 1
        else:
            x += 1
            if count > 0:
                break
    return count


if __name__ == '__main__':
    t = time.process_time()
    # do some stuff
    tmp_list = read_file_day6("day6.txt")
    # print(tmp_list)
    result_list = day6_2_new(tmp_list)
    # P2
    # print("P2")
    print(result_list)
    elapsed_time = time.process_time() - t
    print(elapsed_time)
