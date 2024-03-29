#!/usr/bin/env python
# coding: utf-8


#!pip install pandas
#!pip install numpy


import pandas as pd
import datetime


dados = 'C:\\FADC.xlsx'
#nomes = "C:\\NOMES.xlsx"
df_dados = pd.read_excel(dados)
#df_nomes = pd.read_excel(nomes)


df_dados.head()
# .head exibe o resumo do dataframe


df_dados['ONG'].values[0]
# esse comando exibe os valores da coluna. a sintaxe values exige o parametro com o valor a exibir


for i in df_dados['ONG']:
    df_dados['ONG'].values[0]
    print(i)
    # criando um laço de repetição para exibir todos os nome até o final do conteúdo da planilha, se acrescentar o parâmetro range() vc diz onde ele deve finalizar


df_estudos = df_dados['ONG'].str.split("\n")


df_estudos


#ONG = df_estudos.str.get(0)
#ENDERECO = df_estudos.str.get(1)
#SITE = df_estudos.str.get(2)

df_dados['ONG'] = df_estudos.str.get(0)
df_dados['ENDEREÇO'] = df_estudos.str.get(1)
df_dados['SITE/REDE'] = df_estudos.str.get(2)
df_dados


df_estudos = df_dados['ENDEREÇO'].str.split("Telefones:")
df_estudos.str.get(1)


df_dados['TELEFONE'] = df_estudos.str.get(1)
df_dados['TELEFONE'] = df_dados['TELEFONE'].str.strip()


df_dados['ENDEREÇO'] = df_estudos.str.get(0)
df_estudos = df_dados['ENDEREÇO'].str.split("Endereço:")

df_dados['ENDEREÇO'] = df_estudos.str.get(1)
df_dados['ENDEREÇO'] = df_dados['ENDEREÇO'].str.strip()

# demo.strip()

df_estudos = df_dados['SITE/REDE'].str.split("Site/Redes Sociais:")
df_dados['SITE/REDE'] = df_estudos.str.get(1)
df_dados['SITE/REDE'] = df_dados['SITE/REDE'].str.strip()


#data_atual = date.today()
today = datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S')
today

#hora = datetime.now()


df_dados.to_excel('C:\\FADC_nova - ' + today + '.xlsx')
