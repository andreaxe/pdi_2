import sqlalchemy
import random
import pymysql
from sqlalchemy import create_engine
import pandas as pd
from dataset import generate_dataset


def sql_connection():

    username = 'root'
    password = ''
    hostname = 'localhost'
    database = 'pdi_par'

    cnx = create_engine('mysql+pymsql://{}:{}@{}/{}'.format(username, password, hostname, database))
    conn = pymysql.connect(host=hostname,
                           port=3306,
                           user=username,
                           passwd=password,
                           db=database,
                           charset='utf8')

    return conn


if __name__ == '__main__':

    nodes = 100
    data = generate_dataset(nodes)
    df = pd.DataFrame(data)

    username = 'root'
    password = ''
    hostname = 'localhost'
    database = 'pdi_par'

    from sqlalchemy import create_engine,text

    # sql = text('DROP FOREIGN KEY rdim_ibfk_1;')

    # accessing database:
    engine = create_engine("mysql+pymysql://root:@127.0.0.1/pdi_par")
    con = engine.connect()
    # result = con.execute(sql)

    df.reset_index(inplace=True)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    print(df.columns)
    df.to_csv('teste.csv')
    # uploading dataframe to database:
    df.to_sql(con=con, index=False, name='dim', if_exists='replace', chunksize=10000)

    # generate dependencies (make sure only one root exists)

    list_of_pairs = []
    pair = {'iddim_rdim': 0, 'iddimblg_rdim': 1}
    list_of_pairs.append(pair)

    for i in range(nodes):
        if i == 0:
            continue
        pair = {'iddim_rdim': i, 'iddimblg_rdim':  random.randint(1, 100)}
        list_of_pairs.append(pair)

    pairs = pd.DataFrame(list_of_pairs)
    print(pairs)
    pairs.to_csv('pairs.csv')



