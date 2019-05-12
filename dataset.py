import uuid
import names
import random


def generate_dataset(number_of_nodes):
    """

    :param number_of_nodes:
    :return:
    """

    data = []
    for i in range(number_of_nodes):
        name = names.get_first_name()
        node = {'id_dim': i+1, 'itempt_dim': name, 'itemen_dim': name,
                'desc_dim': str(uuid.uuid4()), 'wgt_dim': random.randint(1, 100), 'pri_dim': random.randint(1, 100),
                'aut_dim': str(uuid.uuid4())}

        data.append(node)

    return data


