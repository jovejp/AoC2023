from collections import defaultdict


def read_file_day5(file_name):
    f = open(file_name)
    line = f.readline()
    line_data = defaultdict(list)
    key_name = ""
    while line:
        if line.strip() != "":
            if line[0].isdigit():
                # add line
                line_data[key_name].append([int(x) for x in line.split()])
            elif line.startswith("seeds:"):
                key_name = "seed"
                line_data[key_name].append([int(x) for x in (line.split(":")[1].split())])
            elif line.startswith("seed-to-soil map:"):
                key_name = "seed-to-soil"
            elif line.startswith("soil-to-fertilizer map:"):
                key_name = "soil-to-fertilizer"
            elif line.startswith("fertilizer-to-water map:"):
                key_name = "fertilizer-to-water"
            elif line.startswith("water-to-light map:"):
                key_name = "water-to-light"
            elif line.startswith("light-to-temperature map:"):
                key_name = "light-to-temperature"
            elif line.startswith("temperature-to-humidity map:"):
                key_name = "temperature-to-humidity"
            elif line.startswith("humidity-to-location map:"):
                key_name = "humidity-to-location"
            else:
                print("Error!!!!", line)
        line = f.readline()
    f.close()
    return line_data


def find_next(x, y):
    result_list = []
    remain_list = []
    while x:
        remain_list.append(x.pop())
        for item in y:
            if remain_list:
                base, base_end = remain_list.pop()
                des, src, step = item
                src_end = src + step
                if base_end < src:
                    result_list.append([base, base_end])
                    break
                elif base_end >= src:
                    if base < src:
                        result_list.append([base, min(src, base_end)])
                    if base < src_end:
                        result_list.append([max(src, base) - src + des, min(src_end, base_end) - src + des])
                    if base_end >= src_end:
                        remain_list.append([max(base, src_end), base_end])
        if remain_list:
            result_list.append(remain_list.pop())
    return result_list


def day_5(main_list):
    # seed = sorted(list(zip(main_list["seed"][0][::2], main_list["seed"][0][1::2])), key=lambda x: x[0])
    seed = []
    for key, data in enumerate(main_list["seed"][0]):
        if key % 2 == 0:
            seed.append([data, data + main_list["seed"][0][key + 1]])
    seed = sorted(seed, key=lambda x: x[0], reverse=True)
    soil = sorted(main_list["seed-to-soil"], key=lambda x: x[1])
    fertilizer = sorted(main_list["soil-to-fertilizer"], key=lambda x: x[1])
    water = sorted(main_list["fertilizer-to-water"], key=lambda x: x[1])
    light = sorted(main_list["water-to-light"], key=lambda x: x[1])
    temperature = sorted(main_list["light-to-temperature"], key=lambda x: x[1])
    humidity = sorted(main_list["temperature-to-humidity"], key=lambda x: x[1])
    location = sorted(main_list["humidity-to-location"], key=lambda x: x[1])

    # print(seed)
    result_soil = find_next(seed, soil)
    result_fertilizer = find_next(result_soil, fertilizer)
    result_water = find_next(result_fertilizer, water)
    result_light = find_next(result_water, light)
    result_temperature = find_next(result_light, temperature)
    result_humidity = find_next(result_temperature, humidity)
    result_location = find_next(result_humidity, location)
    print(result_location)
    return min([x[0] for x in result_location])


if __name__ == '__main__':
    tmp_list = read_file_day5("day5.txt")
    result = day_5(tmp_list)
    # p2
    print("P2")
    print(result)
