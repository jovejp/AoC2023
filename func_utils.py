from collections import defaultdict


# read file to array of array, split by blank line
def read_file_arrays(file_name):
    f = open(file_name)
    my_main_list = []
    my_sub_list = []
    line = f.readline()
    while line:
        if line.strip() == "":
            my_main_list.append(my_sub_list)
            my_sub_list = []
        else:
            my_sub_list.append(line.strip())
        line = f.readline()
    my_main_list.append(my_sub_list)
    f.close()
    return my_main_list


# read file to array
def read_file_array(file_name):
    f = open(file_name)
    my_main_list = []
    line = f.readline()
    while line:
        my_main_list.append(line.strip())
        line = f.readline()
    f.close()
    return my_main_list


# # sample read
#   1024364543 1121869540 764570177
# =>
#   my_main_list = [
#       [1024364543, 1121869540, 764570177]
#       [...]
#   ]
def read_file_as_int_arrays(file_name):
    f = open(file_name)
    my_main_list = []
    line = f.readline()
    while line:
        my_main_list.append([int(x.strip()) for x in line.strip().split()])
        line = f.readline()
    f.close()
    return my_main_list


# # sample read
#   1024364543 1121869540 764570177
# =>
#   my_main_list = [
#       ['1024364543', '1121869540', '764570177']
#       [...]
#   ]
def read_file_as_str_arrays(file_name):
    f = open(file_name)
    my_main_list = []
    line = f.readline()
    while line:
        my_main_list.append([x.strip() for x in line.strip().split()])
        line = f.readline()
    f.close()
    return my_main_list


# # sample read
#   Time:        45     98     83     73
# =>
#   my_main_list[Time] = [45, 98, 83, 73]
def read_file_as_int_dict_arrays(file_name, lsp=":", rsp=" "):
    f = open(file_name)
    my_main_list = defaultdict(list)
    line = f.readline()
    while line:
        line_data = line.strip().split(lsp)
        my_main_list[line_data[0]] = [int(x.strip()) for x in line_data[1].strip().split(rsp)]
        line = f.readline()
    f.close()
    return my_main_list


# # sample read
#   Time:        45     98     83     73
# =>
#   my_main_list[Time] = ['45', '98', '83', '73']
def read_file_dict_arrays(file_name, lsp=":", rsp=" "):
    f = open(file_name)
    my_main_list = defaultdict(list)
    line = f.readline()
    while line:
        line_data = line.strip().split(lsp)
        my_main_list[line_data[0]] = [x.strip() for x in line_data[1].strip().split(rsp)]
        line = f.readline()
    f.close()
    return my_main_list


# read file to array of array, split by step of lines
def read_file_step(file_name, step):
    f = open(file_name)
    my_main_list = []
    my_sub_list = []
    i = 1
    line = f.readline()
    while line:
        if i % step == 0:
            my_sub_list.append(line.strip())
            my_main_list.append(my_sub_list)
            my_sub_list = []
        else:
            my_sub_list.append(line.strip())
        i = i + 1
        line = f.readline()
    my_main_list.append(my_sub_list)
    f.close()
    return my_main_list


# # sample read
#   ..730
# =>
#   my_main_list= [
#       ['.', '.', '7', '3', '0']
#         [...]
#     ]
def read_file_array_of_array(file_name):
    f = open(file_name)
    my_main_list = []
    line = f.readline()
    while line:
        tmp_line = line.strip()
        tmp_list = []
        for x in tmp_line:
            tmp_list.append(x)
        my_main_list.append(tmp_list)
        line = f.readline()
    f.close()
    return my_main_list
