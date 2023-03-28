from constant import *

colunas = "DT_MEDICAO;HR_MEDICAO;CHUVA;PRE_INS;PRE_MAX;PRE_MIN;RAD_GLO;TEM_INS;PTO_INS;TEM_MAX;TEM_MIN;PTO_MAX;PTO_MIN;UMD_MAX;UMD_MIN;UMD_INS;VEN_DIR;VEN_RAJ;VEN_VEL;CD_ESTACAO;DC_NOME;VL_LATITUDE;VL_LONGITUDE;"
# TEM_SEN, UF, TEN_BAT TODO: remover essas colunas do banco antes do upload

for t_write_csv, t_read_csv in zip(list_write, list_read):
    read_csv = open("rowdata/"+t_read_csv, "r")
    write_csv = open("treated/"+t_write_csv, "w+")

    linhas = read_csv.readlines()
    i = 0

    for linha in linhas:
        i += 1
        if i == 3:
            dc_nome = linha.split(";")[1].replace("\n", "")

        elif i == 4:
            cd_estacao = linha.split(";")[1].replace("\n", "")

        if i == 5:
            vl_latitude = linha.split(";")[1].replace(",", ".").replace("\n", "")[0:6]

        elif i == 6:
            vl_longitude = linha.split(";")[1].replace(",", ".").replace("\n", "")[0:6]

        if i == 9:
            write_csv.write(colunas)
            write_csv.write("\n")


        elif i > 10:
            write_csv.write(str(linha.replace(",", ".").replace("\n","")) + dc_nome + ";" + cd_estacao + ";" + vl_latitude + ";" + vl_longitude + ";")
            write_csv.write("\n")

    write_csv.close()
