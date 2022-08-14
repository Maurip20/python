from pyexpat.errors import XML_ERROR_SYNTAX
import pandas as pd
import numpy as np
import locale
from decimal import Decimal
import smtplib
import openpyxl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
locale.setlocale(locale.LC_ALL, 'pt_BR')

#Importar a base de dados para código

dados = "C:\python\orcamento.xlsx"
df_dados = pd.read_excel(dados)

print(df_dados)

df_dados = df_dados.loc[df_dados['ÁREA'] == 'AUTOMAÇÃO COMERCIAL']
total_realizado  = df_dados['REALIZADO NO MÊS'].sum()
total_realizado = Decimal(total_realizado)
print("Soma valor realizado: ")
print(locale.currency(total_realizado, grouping=True))
print("\n")
total_orcado = df_dados['ORÇADO NO MÊS'].sum()
total_orcado = Decimal(total_orcado)
print("Soma valor orçado: ")
print(locale.currency(total_orcado, grouping=True))

host = 'smtp-mail.outlook.com'
port = 587
user = 'dados.gci@sescsp.org.br'
password = 'SESC2020**##'
server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(user, password)
meuemail = "mauricio.santos@sescsp.org.br"




if(total_realizado < total_orcado):
    message = f'O valor  total_orcado é', total_orcado
    print("deu RUIM parça")

email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = meuemail
email_msg['Subject'] = 'Alerta - Orçamento'
#email_msg.attach(MIMEText(message, 'plain'))
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
print("Email Enviado")