"""
September 2022,

This code performs data extraction from INMET meteorological stations.
"""

# Importing libraries:
import pandas as pd
import requests

from MySQL import to_aws

# User interaction:
print("-" * 60)
print("Starting to download data from INMET.\n")
start_date = str(input("Enter start date [AAAA-MM-DD]: "))
end_date = str(input("Enter end date [AAAA-MM-DD]: "))

station = {
    "A826": "alegrete",
    "A827": "bage",
    "A840": "bento_goncalves",
    "A812": "cacapava_do_sul",
    "A838": "camaqua",
    "A897": "cambara_do_sul",
    "A884": "campo_bom",
    "A879": "canela",
    "A811": "cangucu",
    "A887": "pelotas",
    "A853": "cruz_alta",
    "A881": "dom_pedrito",
    "A893": "encruzilhada_do_sul",
    "A828": "erechim",
    "A854": "frederico_westphalen",
    "A883": "ibiruba",
    "A836": "jaguarao",
    "A844": "lagoa_vermelha",
    "A878": "mostardas",
    "A839": "passo_fundo",
    "A801": "porto_alegre",
    "A831": "quarai",
    "A802": "rio_grande",
    "A813": "rio_pardo",
    "A803": "santa_maria",
    "A810": "santa_rosa",
    "A804": "santana_do_livramento",
    "A833": "santiago",
    "A805": "santo_augusto",
    "A830": "sao_borja",
    "A832": "sao_gabriel",
    "A829": "sao_jose_dos_ausentes",
    "A852": "sao_luiz_gonzaga",
    "A889": "sao_vicente_do_sul",
    "A894": "serafina_correa",
    "A837": "soledade",
    "A899": "chui",
    "A882": "teutonia",
    "A808": "torres",
    "A834": "tramandai",
    "A886": "tupancireta",
    "A809": "uruguaiana",
    "A880": "vacaria"
}
for ID, name in station.items():
    # Request
    req = requests.get("https://apitempo.inmet.gov.br/estacao/" + start_date + "/" + end_date + "/" + ID)

    # Pandas manipulation
    df = pd.read_json(req.text)
    df['HR_MEDICAO'] = df['HR_MEDICAO'] / 100.
    df = df.set_index('DT_MEDICAO')

    # Save (XLSX)
    df.to_excel("data/" + ID + "-" + name + ".xlsx")

    # Save (JSON)
    open("data/" + ID + "-" + name + ".json", "w").write(req.text)

    if False:  # WARN: For safety, switch to True to execute this line.
        # Save (AWS)
        to_aws(df)

    # Interaction
    print(ID + "-" + name + " OK!")

print("Success")
print("-" * 60)
