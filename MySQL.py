import json

import pandas as pd
from sqlalchemy import create_engine

conf = json.load(open("config.json", encoding='utf-8'))


def connect_AWS():
    """
    This function must connect with success in AWS database.
    :return: it must return a connection with success.
    """
    engine = create_engine("mysql+mysqlconnector://{user}:{pw}@{host}/{db}"
                           .format(user=conf.get("user"),
                                   pw=conf.get("pw"),
                                   host=conf.get("host"),
                                   db=conf.get("db")))
    return engine


def write_AWS(df, table):
    """
    This function must write the dataframe to database.
    :param table: you must pass a valid table name (String)
    :param df: you must pass a valid dataframe (DataFrame)
    :return: it must a successful message.
    """
    engine = connect_AWS()

    df.to_sql(table, con=engine, if_exists='append')
    return print("Dataframe wrote with success!")


def read_AWS(table, station_ID):
    """
    This function must create a database connection.
    :param station_ID: you must pass a valid station ID (String)
    :param table: you must pass a valid table name (String)
    :return df: it must return a dataframe with the table
    """
    engine = connect_AWS()

    with engine.begin() as conn:
        query = "SELECT * FROM data_warehouse." + table + " WHERE CD_ESTACAO = '" + station_ID + "'"
        df = pd.read_sql_query(query, conn)

    return df
