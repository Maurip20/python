# -*- coding: utf-8 -*-
"""Aula 1 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_pFJjhy4NvanT1tiA9GiqLNXulB2jJlC
"""

print("Hello Word")

aluno =  input("Digite seu nome: ")
nt_mensal = float(input("Digite seu nota mensal: "))
nt_bimestral = float(input("Digite seu nota bimestral: "))

soma = nt_mensal + nt_bimestral
qtdade = 2

media = soma / qtdade
print("Olá", aluno, "sua nota mensal foi", nt_mensal, "e sua nota bimestral foi", nt_bimestral)
print(f"O Aluno {aluno} ficou com média =", media)


ponto_extra = float(input("Este aluno tem pontos adicionais na nota, favor inserir: "))

notafinal = media + ponto_extra

print(notafinal)

"""# Nova seção"""

lista_compras = ['arroz','bolo', 'coca-cola']
lista_compras2 = ["feijão", "mussarela", "água com gás"]

prato1 = lista_compras[0]
prato2 = lista_compras2[1]
prato3 = lista_compras2[2]

print(f"Hoje meu almoço será {prato1} com {prato2} e {prato3}.")