import json

import pandas as pd
from sqlalchemy import create_engine

conf = json.load(open("config.json", encoding='utf-8'))


def read_AWS():
    engine = create_engine("mysql+mysqlconnector://{user}:{pw}@{host}/{db}"
                           .format(user=conf.get("user"),
                                   pw=conf.get("pw"),
                                   host=conf.get("host"),
                                   db=conf.get("db")))

    with engine.begin() as conn:
        query = "SELECT * FROM data_warehouse.extract_data"
        df = pd.read_sql_query(query, conn)

    return df


kevinReiDelas = read_AWS()
print(kevinReiDelas.head(10))
