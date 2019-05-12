import random
import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine
from dataset import generate_dataset


def my_custom_random(nodes, exclude):

    exclude=[exclude]
    rand_number = random.randint(1, nodes)
    return my_custom_random(nodes, exclude) if rand_number in exclude else rand_number


def generate_pairs(nodes):
    # generate dependencies (make sure only one root exists)
    list_of_pairs = []

    # pair = {'iddim_rdim': 0, 'iddimblg_rdim': 1}
    # list_of_pairs.append(pair)

    for i in range(nodes):
        i += 1
        if i == 1:
            continue
        pair = {'iddim_rdim': i, 'iddimblg_rdim': my_custom_random(nodes, i)}
        list_of_pairs.append(pair)

    pairs = pd.DataFrame(list_of_pairs)
    pairs.to_sql(con=con, index=False, name='rdim', if_exists='append', chunksize=10000)


def generate_data():

    import database
    nodes = 15
    data = generate_dataset(nodes)
    df = pd.DataFrame(data)

    # sql = text('DROP FOREIGN KEY rdim_ibfk_1;')

    # accessing database:

    # result = con.execute(sql)

    df.reset_index(inplace=True)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    # print(df.columns)
    # df.to_csv('teste.csv')
    # uploading dataframe to database:

    df.to_sql(con=con, index=False, name='dim', if_exists='append', chunksize=10000)

    generate_pairs(nodes)


if __name__ == '__main__':

    engine = create_engine("mysql+pymysql://root:@127.0.0.1/pdi_par")
    con = engine.connect()
    generate_data()
    # accessing database:
    sql = text('select * from dim;')
    results = con.execute(sql)
    result_set = results.fetchall()
    dim_arr = []

    for row in result_set:
        dim_arr.append(dict(row))

    print(dim_arr)
    sql = text('select * from rdim;')
    results = con.execute(sql)
    result_set = results.fetchall()
    rdim_arr = []

    for row in result_set:
        rdim_arr.append(dict(row))

    print(rdim_arr)

    from network import build_network
    build_network(dim_arr, rdim_arr)
    # print(results)
    # for result in results:
    #     print(result)

    # generate_data()




