import pandas as pd
from constant import list_write

from MySQL import to_aws
for name in list_write:
    # Load csv
    df = pd.read_csv("treated/"+name, sep=";")
    df = df.drop(columns=["Unnamed: 23"])
    df["HR_MEDICAO"] = df["HR_MEDICAO"].apply(lambda x: int(x.replace(":", "")[0:4])) / 100.
    df = df.set_index('DT_MEDICAO')

    # Save (AWS)
    to_aws(df)

    # Interaction
    print(name + " OK!")

print("Success")
print("-" * 60)
