#!/usr/bin/env python
# coding: utf-8


#instalando as bibliotecas
#!pip install pyodbc
#!pip install pyodbc
#!pip install datetime
#!pip install parse
#!pip install matplotlib
#!pip install seaborn
#!pip install -q -U watermark

#importando bibliotecas
import pandas as pd
import numpy as np
import time
import datetime
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import win32com.client
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email import encoders
import email
import email.mime.application
#from pretty_html_table import build_table

dest_email = "mauricio.santos@sescsp.org.br"
arquivo_entrada = r"C:\Users\mauricio.santos\OneDrive - SERVICO SOCIAL DO COMERCIO-SESC\GitHub\powerquery\TCU\TCU_CORRIGIR.xlsx"
#arquivo_saida = "C:\projetos\documentacao_legal\pendencias.xlsx"
#arquivo_unidade = "C:\projetos\documentacao_legal\sesc_uo.xlsx"
#dados = "C:\python\orcamento.xlsx"


xlapp = win32com.client.DispatchEx("Excel.Application")
wb = xlapp.Workbooks.Open(arquivo_entrada)
wb.RefreshAll()
xlapp.CalculateUntilAsyncQueriesDone()
time.sleep(20)
xlapp.DisplayAlerts = False
wb.Save()
wb.Close()
xlapp.quit()

##importanto planilha de trabalho
planilha = pd.read_excel(arquivo_entrada)
planilha.shape
planilha.isnull().sum()


#dados de configuração da Conta de E-mail
host = 'smtp-mail.outlook.com'
port = 587
user = 'dados.gci@sescsp.org.br'
password = 'SESC2020**##'
server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(user, password)
meuemail = "mauricio.santos@sescsp.org.br"

corpo = """ <html>
                 <body>
                 <b>Prezados(as), favor não responder esse e-mail automático.</b>  <br> <br> 
                
                 Atualização executada com sucesso. <br> 
                 Verifique as colunas de correção  <br> <br>

                 <b> Monitoramento e Controle de Indicadores </b> <br>
                 Gerência de Conformidade Institucional <br>
                 Av. Álvaro Ramos, 991 - 1º Andar - Quarta Parada - São Paulo <br>
                 <a href="https://www.sescsp.org.br/">sescsp.org.br</a></p>
 
               
                         </body>
                         </html>
               """

pdfname='\TCU_CORRIGIR.xlsx'
fp=open(pdfname,'rb')
anexo = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
fp.close()
anexo.add_header('Content-Disposition','attachment',filename=pdfname)


email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = meuemail
email_msg['Subject'] = 'Notificação - Atualização TCU'
email_msg.attach(MIMEText(corpo,"html"))
email_msg.attach(anexo)
server.ehlo()
#server.starttls()
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
print("Email Enviado")








