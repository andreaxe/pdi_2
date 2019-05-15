import uuid
import names
import random
import pandas as pd


def generate_dataset(number_of_nodes):
    """

    :param number_of_nodes:
    :return:
    """

    data = []
    for i in range(number_of_nodes):
        name = names.get_first_name()
        node = {'id_dim': i+1, 'itempt_dim': name, 'itemen_dim': name,
                'desc_dim': str('-'), 'wgt_dim': random.randint(1, 100), 'pri_dim': random.randint(1, 100),
                'aut_dim': str('-')}

        data.append(node)

    return data


def generate_data(number_of_nodes, con):
    """
    generate dim data
    :param number_of_nodes:
    :param con:
    :return:
    """

    import database
    data = generate_dataset(number_of_nodes)
    df = pd.DataFrame(data)
    df.reset_index(inplace=True)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df.to_sql(con=con, index=False, name='dim', if_exists='append', chunksize=10000)
    generate_pairs(number_of_nodes, con)


def generate_pairs(nodes, con):
    """
    generate dependencies rdim data
    :param nodes:
    :param con:
    :return:
    """
    list_of_pairs = []

    for i in range(nodes):
        i += 1
        if i == 1:
            continue
        pair = {'iddim_rdim': i, 'iddimblg_rdim': my_custom_random(nodes, i)}
        list_of_pairs.append(pair)

    pairs = pd.DataFrame(list_of_pairs)
    pairs.to_sql(con=con, index=False, name='rdim', if_exists='append', chunksize=10000)


def my_custom_random(nodes, exclude):

    exclude=[exclude]
    rand_number = random.randint(1, nodes)
    return my_custom_random(nodes, exclude) if rand_number in exclude else rand_number
