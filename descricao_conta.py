
#selecionar a coluna de descrição das contas
#identificar os valores que possuem repetição


#importar os dados da planilha de contas 
from multiprocessing.sharedctypes import Value
import pandas as pd
dados = "C:\projetos\contas.xlsx"
df_dados = pd.read_excel(dados)

#selecionar e identificar valores repetidos na coluna descrição
#repetido = df_dados.value_counts(['CONTA DESCRICAO'])

#imprimir na tela as colunas que possuem mais de 1 ocorrência

#pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(repetido)
print("\n")
#PERCORRENDO toda a lista pelo tamanho do dataframe
#for i in range(len(df_dados)):
#    print("A descrição e conta são:"+df_dados['CONTA DESCRICAO']+str(df_dados['COD_CTA']))
#PERCORRENDO toda a lista pelo tamanho do dataframe

for i in range(len(df_dados)):
    if df_dados['COD_EQV'].iloc[i] in ['7']:
        df_novo = df_dados
        print(df_dados)

