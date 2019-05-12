from sqlalchemy import text
from sqlalchemy import create_engine


if __name__ == '__main__':

    dim_arr  = []
    rdim_arr = []

    engine = create_engine("mysql+pymysql://root:@127.0.0.1/pdi_par")
    con = engine.connect()

    # this function populates the database
    # generate_data(number_of_nodes=15, con=con)

    # accessing database:
    sql = text('select * from dim;')
    results = con.execute(sql)
    result_set = results.fetchall()

    for row in result_set:
        dim_arr.append(dict(row))

    sql = text('select * from rdim;')
    results = con.execute(sql)
    result_set = results.fetchall()

    for row in result_set:
        rdim_arr.append(dict(row))

    from network import build_network
    build_network(dim_arr, rdim_arr)
    # print(results)
    # for result in results:
    #     print(result)

    # generate_data()




