import pandas as pd
from constant import list_write

from MySQL import to_aws
for name in list_write:
    # Load csv
    df = pd.read_csv("treated/"+name, sep=";")
    df = df.drop(columns=["Unnamed: 23"])

    # Save (AWS)
    to_aws(df) #TODO: precisa ajustar o tipo das colunas no banco

    # Interaction
    print(name + " OK!")

print("Success")
print("-" * 60)
