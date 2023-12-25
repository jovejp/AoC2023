from func_utils import read_file_array
import networkx as nx

debug = False
file_name = "input_sample.txt" if debug else "input.txt"

input_list = read_file_array(file_name)
total_rows = len(input_list)
valid_list = {xx.split(":")[0].strip(): xx.split(":")[1].split() for xx in input_list}


def func():
    # g = nx.Graph()
    # for k, v in valid_list.items():
    #     for vv in v:
    #         g.add_edge(k, vv)
    #     # g.add_edges_from([(kk, vvv) for vvv in vv])
    # g.remove_edges_from(nx.minimum_edge_cut(g))
    # return prod([len(c) for c in nx.connected_components(g)])

    g = nx.DiGraph()
    for k, v in valid_list.items():
        for vv in v:
            g.add_edge(k, vv, capacity=1.0)
            g.add_edge(vv, k, capacity=1.0)

    for x in [list(valid_list.keys())[0]]:
        for y in valid_list.keys():
            if x != y:
                cut_value, (group_a, group_b) = nx.minimum_cut(g, x, y)
                if cut_value == 3:
                    return len(group_a) * len(group_b)


if __name__ == '__main__':
    r_p1 = func()
    print("part1", r_p1)
