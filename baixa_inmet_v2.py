#!/usr/bin/python3
# -*- coding: utf-8 -*-
# *** template python ***

"""
Julho de 2020,

Programa para realizar download do banco de dados INMET.

--
Rafael Corrêa de Lima
Bolsista de Graduação - LMQA/CEPSRM
rafael.correa@ufrgs.br
"""

#Importando bibliotecas:
from math import *      #Importa o pacote de matematica
import os               #Importa os comandos do linux
import pandas as pd	#Importa biblioteca de data frames

#Interação com o usuário:
print("-"*60)
print("Programa que realiza download dos dados INMET.\n")
i=str(input("Entre com a data de inicio [AAAA-MM-DD]: "))
j=str(input("Entre com a data de fim [AAAA-MM-DD]: "))

est_id=['A826','A827','A840','A812','A838','A884','A879','A811','A899','A853','A881',
'A828','A854','A883','A836','A844','A878','A856','A839','A801','A831','A802','A813','A803',
'A804','A810','A833','A805','A830','A832','A829','A852','A889','A894','A837','A882','A808','A834',
'A886','A809','A880']

est_name=['alegrete','bage','bento_goncalves','cacapava_do_sul','camaqua',
'campo_bom','canela','cangucu','chui','cruz_alta','dom_pedrito',
'erechim','frederico_westphalen','ibiruba','jaguarao','lagoa_vermelha','mostardas',
'palmeira_das_missoes','passo_fundo','porto_alegre','quarai','rio_grande',
'rio_pardo','santa_maria','santana_do_livramento','santa_rosa','santiago',
'santo_augusto','sao_borja','sao_gabriel','sao_jose_dos_ausentes','sao_luiz_gonzaga',
'sao_vicente_do_sul','serafina_correa','soledade','teutonia','torres','tramandai',
'tupancireta','uruguaiana','vacaria']

n=0
for id in est_id:
	os.system('wget https://apitempo.inmet.gov.br/estacao/'+i+'/'+j+'/'+id)
	os.system('mv '+id+' '+id+'-'+est_name[n])
	df=pd.read_json(id+'-'+est_name[n])
	out=pd.DataFrame()
	out['DT_MEDICAO']=df['DT_MEDICAO']
	out['HR_MEDICAO']=df['HR_MEDICAO']/100.
	out['TEM_INS']=df['TEM_INS']
	out['TEM_MAX']=df['TEM_MAX']
	out['TEM_MIN']=df['TEM_MIN']
	out['UMD_INS']=df['UMD_INS']
	out['UMD_MAX']=df['UMD_MAX']
	out['UMD_MIN']=df['UMD_MIN']
	out['PTO_INS']=df['PTO_INS']
	out['PTO_MAX']=df['PTO_MAX']
	out['PTO_MIN']=df['PTO_MIN']
	out['PRE_INS']=df['PRE_INS']
	out['PRE_MAX']=df['PRE_MAX']
	out['PRE_MIN']=df['PRE_MIN']
	out['VEN_VEL']=df['VEN_VEL']
	out['VEN_DIR']=df['VEN_DIR']
	out['VEN_RAJ']=df['VEN_RAJ']
	out['RAD_GLO']=df['RAD_GLO']
	out['CHUVA']=df['CHUVA']
	out=out.set_index('DT_MEDICAO')
	out.to_excel(id+'-'+est_name[n]+'.xlsx')
	n+=1

print("Fim :D")
print("-"*60)
