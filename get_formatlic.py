from pyexpat.errors import XML_ERROR_SYNTAX
import pandas as pd
import numpy as np
import locale
from decimal import Decimal
import smtplib
import openpyxl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
locale.setlocale(locale.LC_ALL, 'pt_BR')

#IMPORTAR E IMPRIMIR BASE DE DADOS COM PREENHCIMENTO DAS GERENCIAS
df_dados = pd.read_excel(r"C:\python\licitantes.xlsx")
print(df_dados)
#VERIFICAR O TIPO DAS COLUNAS 
df_dados.info()

#IMPRIMIR TODOS OS  CNPJs com laço

#print(df_dados['CNPJ'].values[0])
#
# for i in df_dados['CNPJ']:
#     df_dados['CNPJ'].values[0]
#     df_dados = df_dados.astype({'CNPJ': 'object'}).dtypes
#     df_dados['CNPJ'].count(".")
#     print(i)
#df_dados['CNPJ'] = df_dados['CNPJ'].astype(str)
#CONVERTER PARA TEXTO A COLUNA CNPJ
df_dados['CNPJ'] = df_dados['CNPJ'].astype(str)
#print(df_dados['CNPJ'].values[0])
#EXIBE O NOME DAS COLUNAS E OS TIPOS
df_dados.info()
#IMPRIMI O CNPJ
#print(df_dados['CNPJ'].values[0])
palavra = "." 
contador = 0
#CHECA SE O CNPJ TEM PONTO

if palavra not in df_dados['CNPJ'].values[0]:
    print("nao tem")
else:
    print("deu certo")
    contador = contador + 1
print(contador)

#CONTAR NUMERO DE CARACTERES do CNPJ
index = 0

for i in (df_dados['CNPJ']):
    nc = len(df_dados['CNPJ'].values[index])
    index = index + 1
    print(i)
    if(nc != 14):
        print("CNPJ ERRADO")
        print(f"possui {nc} caracteres esse CNPJ")

df_dados.info()

