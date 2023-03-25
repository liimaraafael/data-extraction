import json

from sqlalchemy import create_engine

conf = json.load(open("config.json", encoding='utf-8'))


def to_aws(df):
    engine = create_engine("mysql+mysqlconnector://{user}:{pw}@{host}/{db}"
                           .format(user=conf.get("user"),
                                   pw=conf.get("pw"),
                                   host=conf.get("host"),
                                   db=conf.get("db")))

    df.to_sql(conf.get("table"), con=engine, if_exists='append')
