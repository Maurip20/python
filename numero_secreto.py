import random
numero_secreto = random.randint(1,50)



print("Duvido você acertar o número secreto em 3 tentativas!!!")

tentativas = 0
numero_escolhido = int(input("Escolha o número: "))

while numero_escolhido != numero_secreto and tentativas < 2 :
    print("Número errado! Tente mais uma vez")
    if numero_escolhido >= numero_secreto:
        print("O número secreto é menor")
        tentativas = tentativas + 1
        print("Resta apenas", 3 - tentativas, "tentativas")
    else:
        print("Número secreto é maior")
        tentativas = tentativas + 1
        print("Resta apenas", 3 - tentativas, "tentativas")
    numero_escolhido = int(input("Escolha o número: "))

print(f"Excedeu o número  {tentativas +1} tentativas")
if numero_escolhido == numero_secreto:
    print(f"Acertou mizeravi, o número secreto é {numero_secreto}")

