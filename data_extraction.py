"""
September 2022,

This code performs data extraction from INMET meteorological stations.
"""

# Importing libraries:
import pandas as pd
import requests

# User interaction:
print("-" * 60)
print("Starting to download data from INMET.\n")
start_date = str(input("Enter start date [AAAA-MM-DD]: "))
end_date = str(input("Enter end date [AAAA-MM-DD]: "))

station_ID = ['A826', 'A827', 'A840', 'A812', 'A838', 'A884', 'A879', 'A811', 'A899', 'A853', 'A881', 'A828', 'A854',
              'A883', 'A836', 'A844', 'A878', 'A856', 'A839', 'A801', 'A831', 'A802', 'A813', 'A803', 'A804', 'A810',
              'A833', 'A805', 'A830', 'A832', 'A829', 'A852', 'A889', 'A894', 'A837', 'A882', 'A808', 'A834', 'A886',
              'A809', 'A880']

station_name = ['alegrete', 'bage', 'bento_goncalves', 'cacapava_do_sul', 'camaqua', 'campo_bom', 'canela', 'cangucu',
                'chui', 'cruz_alta', 'dom_pedrito', 'erechim', 'frederico_westphalen', 'ibiruba', 'jaguarao',
                'lagoa_vermelha', 'mostardas', 'palmeira_das_missoes', 'passo_fundo', 'porto_alegre', 'quarai',
                'rio_grande', 'rio_pardo', 'santa_maria', 'santana_do_livramento', 'santa_rosa', 'santiago',
                'santo_augusto', 'sao_borja', 'sao_gabriel', 'sao_jose_dos_ausentes', 'sao_luiz_gonzaga',
                'sao_vicente_do_sul', 'serafina_correa', 'soledade', 'teutonia', 'torres', 'tramandai',
                'tupancireta', 'uruguaiana', 'vacaria']

for ID, name in zip(station_ID, station_name):
    # Request
    req = requests.get("https://apitempo.inmet.gov.br/estacao/" + start_date + "/" + end_date + "/" + ID)

    # Pandas manipulation
    df = pd.read_json(req.text)
    df['HR_MEDICAO'] = df['HR_MEDICAO'] / 100.
    df = df.set_index('DT_MEDICAO')

    # Save (XLSX and JSON)
    df.to_excel(ID + "-" + name + ".xlsx")
    with open(ID + "-" + name + ".json", "w") as outfile:
        outfile.write(req.text)

    # Interaction
    print(ID + "-" + name + " OK!")

print("Success")
print("-" * 60)