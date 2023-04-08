from MySQL import connect_AWS
from constant import list_write
from functions import *

engine = connect_AWS()

for name in list_write:
    # Load csv
    df = pd.read_csv("treated/" + name, sep=";")\
        .transform(filter_temp) \
        .transform(filter_pto) \
        .transform(filter_press) \
        .transform(filter_prec) \
        .transform(filter_radia) \
        .transform(filter_umid) \
        .transform(filter_ven) \
        .transform(treat_df) \
        .set_index("DT_MEDICAO") \

    # Save (AWS)
    df.to_sql("processed_data_br", con=engine, if_exists='append')

    # Interaction
    print(name + " OK!\n")

print("Success")
print("-" * 60)
