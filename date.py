from datetime import date
import time
from calendar import weekday
from tkinter import N
import calendar

hoje = date.today()
# ano = date.year(hoje)
# mes = date.month(hoje)
# dia = date.day(hoje)
# nomedodia = weekday(ano,mes,dia)
# print(nomedodia)


print(calendar.day_name[hoje.weekday()])

if calendar.day_name[hoje.weekday()] == "Saturday":
    print("deu certo")
else:
    print("hoje não")