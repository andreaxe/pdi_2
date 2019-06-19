import os
import time
import json
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout


def my_interator(d, dim, id_key='name', amount_key='size'):
    """
    Recursive function to build the dictionary to be exported to json
    :param d:
    :param dim:
    :param id_key
    :param amount_key:
    :return:
    """
    if isinstance(d, dict):
        for key, value in d.items():
            if isinstance(d.get(key), list):
                my_interator(d.get(key), dim, id_key, amount_key)
            else:
                if key == id_key:
                    for k in dim:
                        if k['id_dim'] == d[key]:
                            d[key] = k['itempt_dim']
                            break
    else:
        # children
        # if not 'children' in d:
        for value in d:
            if not 'children' in value:
                for key in dim:
                    if key['id_dim'] == value[id_key]:
                            value[amount_key] = key['wgt_dim']

            my_interator(value, dim, id_key, amount_key)


def build_network(dim, rdim):

    G = nx.DiGraph()
    labels = {}

    # add all nodes
    for dict_item in dim:
        G.add_node(dict_item['id_dim'])
        labels[dict_item['id_dim']] = dict_item['itempt_dim'] + ' ' + str(dict_item['id_dim'])

    # add edges
    # @todo posso precisar de trocar as dependencias
    for dict_item in rdim:
        G.add_edge(dict_item['iddim_rdim'], dict_item['iddimblg_rdim'],)

    write_dot(G, 'network.dot')
    plt.title('draw_networkx')
    pos = graphviz_layout(G, prog='dot')
    nx.draw(G, pos, edge_color='b',  node_size=1500, arrowsize=15, arrowstyle='fancy')
    # nx.draw_networkx_labels(G, pos, arrows=True)
    # nx.draw_networkx_nodes(G, pos, node_size=1000, font_size=8, arrows=True)

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels, font_size=6)
    # plt.figure(6, figsize=(24, 24))

    figure = plt.gcf()  # get current figure

    figure.set_size_inches(32, 24)
    # when saving, specify the DPI
    plt.title(label="")
    plt.savefig(os.path.join('plots', time.strftime('%a %H:%M:%S') + '.png'), dpi=100)
    plt.show()

    # ==== Testes

    # from networkx.readwrite import json_graph
    # data = json_graph.adjacency_data(G, {'id':1, 'key': 'teste'})
    from networkx.readwrite import json_graph

    sunburst = json_graph.tree_data(G, root=1, attrs={'id': 'name', 'children': 'children'})
    my_interator(sunburst, dim)

    with open(os.path.join('html', 'data', 'sunburst.json'), "w") as outfile:
        json.dump(sunburst, outfile, indent=4)

    treemap = json_graph.tree_data(G, root=1, attrs={'id': 't', 'children': 'children'})
    my_interator(treemap, dim, id_key='t', amount_key='value')

    with open(os.path.join('html', 'data', 'treemap.json'), "w") as outfile:
        json.dump(treemap, outfile, indent=4)

    plt.close()
