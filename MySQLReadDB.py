from MySQL import read_AWS

df = read_AWS("row_data_br", "A001")

df.to_excel("A001.xlsx")
