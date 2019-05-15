import os
import time
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

# DIM
# [{'id_dim': 1, 'itempt_dim': 'Lisa', 'itemen_dim': 'Lisa', 'desc_dim': '62946624-12c8-4a6c-af19-ba12d4f36465',
# 'wgt_dim': 44, 'pri_dim': 89, 'aut_dim': '67b6b303-a50c-42c1-aea5-b24b25dba186'},

# {'id_dim': 2, 'itempt_dim': 'Judy', 'itemen_dim': 'Judy', 'desc_dim': '80dba112-19de-43e3-a868-f6e8df5149f6',
# 'wgt_dim': 29, 'pri_dim': 57, 'aut_dim': 'bc784724-2ca8-4033-89a3-01402e4d9aad'},

# RDIM
# [{'iddim_rdim': 2, 'iddimblg_rdim': 1},
#  {'iddim_rdim': 9, 'iddimblg_rdim': 1},
#  {'iddim_rdim': 7, 'iddimblg_rdim': 4},

# Assume dependency is in iddim_rdim


def search_for_label(value, dim):
    """
    not used...
    :param value:
    :param dim:
    :return:
    """

    for dict_item in dim.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if dict_item['id_dim'] == value:
            return dict_item['itempt_dim']


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
    nx.draw(G, pos, edge_color='b',  node_size=1300, arrowsize=15, arrowstyle='fancy')
    # nx.draw_networkx_labels(G, pos, arrows=True)
    # nx.draw_networkx_nodes(G, pos, node_size=1000, font_size=8, arrows=True)

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels, font_size=6)
    # plt.figure(6, figsize=(24, 24))

    figure = plt.gcf()  # get current figure

    figure.set_size_inches(16, 12)
    # when saving, specify the DPI
    plt.title(label="")
    plt.savefig(os.path.join('plots', time.strftime('%a %H:%M:%S') + '.png'), dpi=100)
    plt.show()
    plt.close()


def example_network():

    G = nx.DiGraph()

    nodes = [{'node': "ROOT", "labels": "ROOT", "edge": ""},
             {'node': "ROOT2", "labels": "ROOT2", "edge": ""},
             {'node': "ROOT3", "labels": "ROOT3", "edge": ""},
             {'node': "Root_Child_%1", "labels": "Root_Child_%1", "edge": "ROOT"},
             {'node': "Root_Child_%1", "labels": "Root_Child_%1", "edge": "ROOT2"},
             {'node': "Root_Child_%1", "labels": "Root_Child_%1", "edge": "ROOT3"},
             {'node': "Root_Child_%2", "labels": "Root_Child_%2", "edge": "ROOT"},
             {'node': "Root_Child_%2_1", "labels": "Root_Child_%2_1", "edge": "Root_Child_%1"},
             {'node': "Root_Child_%2_2", "labels": "Root_Child_%2_2", "edge": "Root_Child_%2"},
             {'node': "Root_Child_%2_3", "labels": "Root_Child_%2_3", "edge": "ROOT"}
             ]

    labels = {}

    for dict_item in nodes:

        if dict_item['edge'] == "":
            G.add_node(dict_item['node'])
        else:
            G.add_node(dict_item['node'])
            G.add_edge(dict_item['edge'], dict_item['node'])

        labels[dict_item['node']] = dict_item['labels']

    write_dot(G, 'test.dot')
    #
    # # same layout using matplotlib with no labels
    plt.title('draw_networkx')
    pos = graphviz_layout(G, prog='dot')
    # nx.draw(G, pos, labels, arrows=True)
    # nx.draw_networkx_labels(G, pos, arrows=True)
    nx.draw_networkx_nodes(G, pos, node_size=1000, font_size=8)

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels, font_size=8)
    plt.show()
