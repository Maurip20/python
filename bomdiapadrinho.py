from calendar import WEDNESDAY, weekday
from datetime import date
from unittest.mock import patch
import pyautogui
import pyperclip
import calendar
import time
pyautogui.PAUSE = 1

pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.alert("Vai começar, aperto ok e não mexa em nada")
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://web.whatsapp.com/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
#Passo 2: Navegar até a conversa com meu padrinho
time.sleep(8)
pyautogui.click(x=427, y=268)
# print(pyautogui.position())

# veriicando dia da semana e mensagem compatível

hoje = date.today()
# diadasemana = calendar.day_name[hoje.weekday()]

nomedia = calendar.day_name[hoje.weekday()]
# escrevendo a mensagempara o padrinho
mensagens = ['Bom dia padrinho, excelente semana que deus abençoe seu dia', 'Excelente sábado e ótimo final de semana','Hoje tem jogooo', 'Falta poucooooo', 'Sextouuuuu', 'Sabadouuuuuu', 'domingou']
diadasemana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

tamanho = len(mensagens)

for mensagem in range(tamanho):
    if diadasemana[mensagem] == nomedia:
        pyautogui.write(mensagens[mensagem])

time.sleep(2)

# print(pyautogui.position())