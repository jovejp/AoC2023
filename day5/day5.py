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
    result = 0
    for item in y:
        if x < item[1]:
            result = x
            break
        elif item[1] <= x < item[1] + item[2]:
            result = item[0] + x - item[1]
            break
    if result == 0:
        result = x
    return result


def day_5(main_list):
    seed = sorted(main_list["seed"][0])
    soil = sorted(main_list["seed-to-soil"], key=lambda x: x[1])
    fertilizer = sorted(main_list["soil-to-fertilizer"], key=lambda x: x[1])
    water = sorted(main_list["fertilizer-to-water"], key=lambda x: x[1])
    light = sorted(main_list["water-to-light"], key=lambda x: x[1])
    temperature = sorted(main_list["light-to-temperature"], key=lambda x: x[1])
    humidity = sorted(main_list["temperature-to-humidity"], key=lambda x: x[1])
    location = sorted(main_list["humidity-to-location"], key=lambda x: x[1])

    location_result = defaultdict(list)
    for x in seed:
        location_result[x].append(x)
        location_result[x].append(find_next(x, soil))
        location_result[x].append(find_next(location_result[x][-1], fertilizer))
        location_result[x].append(find_next(location_result[x][-1], water))
        location_result[x].append(find_next(location_result[x][-1], light))
        location_result[x].append(find_next(location_result[x][-1], temperature))
        location_result[x].append(find_next(location_result[x][-1], humidity))
        location_result[x].append(find_next(location_result[x][-1], location))
    return min([row[-1] for row in location_result.values()])


if __name__ == '__main__':
    tmp_list = read_file_day5("day5.txt")
    result_list = day_5(tmp_list)
    # # p1
    print("P1")
    print(result_list)
