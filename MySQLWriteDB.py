from MySQL import connect_AWS
from constant import list_write_rs
from functions import *

engine = connect_AWS()

i = 0
for name in list_write_rs:
    # Load csv
    df = pd.read_csv("treated/" + name, sep=";") \
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
    df.to_sql("processed_data_rs", con=engine, if_exists='append')

    # Interaction
    status = round((i / float(len(list_write_rs))) * 100, 2)

    if status < 100.00:
        print("File: " + name + " is OK!\nStatus: " + str(status) + "% complete. Just a moment, please.\n")

    else:
        print("File: " + name + " is OK!\nStatus: " + str(status) + "% complete.\n")
    i += 1

print("Success")
print("-" * 60)
