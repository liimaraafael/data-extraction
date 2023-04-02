import pandas as pd

from MySQL import connect_AWS
from constant import list_write

engine = connect_AWS()

for name in list_write:
    # Load csv
    df = pd.read_csv("treated/" + name, sep=";")
    df = df.drop(columns=["Unnamed: 23"])
    df["HR_MEDICAO"] = df["HR_MEDICAO"].apply(lambda x: int(x.replace(":", "")[0:4])) / 100.
    df = df.set_index('DT_MEDICAO')

    # Save (AWS)
    df.to_sql("row_data_br", con=engine, if_exists='append')

    # Interaction
    print(name + " OK!\n")

print("Success")
print("-" * 60)
