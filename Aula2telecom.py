from numpy import float64
import pandas as pd
import plotly.express as px


# importar a base de dados e imprimir base

df_telecom = pd.read_csv(r'C:\Users\mauricio.santos\OneDrive - SERVICO SOCIAL DO COMERCIO-SESC\Mauricio\Cursos\Hashtag Treinamento - Python\drive-download-20220310T200051Z-001\telecom_users.csv')
# print(df_telecom)

# 0 ou ‘index’ será apagada a linha
# indicada;
# • 1 ou ‘columns’ será apagada a coluna
# indicada.

df_telecom.info()
df_telecom = df_telecom.drop(['Unnamed: 0'], axis=1) # Drop para coluna especifica 
df_telecom = df_telecom.dropna(how='all', axis=1) # Drop para coluna 100% vazia
df_telecom = df_telecom.dropna(how='all', axis=0) #Drop para linha 100% vazia
df_telecom.info()
df_telecom['TotalGasto'] = pd.to_numeric(df_telecom['TotalGasto'],errors="coerce")
df_telecom = df_telecom.dropna() # esse drop sem parâmetro elimina todas as linhas que contenham no mínimo um valor vazio
df_telecom.info()

print(df_telecom['Churn'].value_counts())
print(df_telecom['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) # exibe o percetual por conta do parametro nornalize e o map formata

for coluna in df_telecom:
    if coluna != 'IDCliente':
        fig = px.histogram(df_telecom, x=coluna, color='Churn')
        fig.show()   