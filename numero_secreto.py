import random
numero_secreto = random.randint(1,50)

print("Duvido você acertar o número secreto!!!")


numero_escolhido = int(input("Escolha o número: "))

while numero_escolhido != numero_secreto:
    print("Número errado tente novamente")
    if numero_escolhido >= numero_secreto:
        print("O número secreto é menor")
    else:
        print("Número secreto é maior")
    numero_escolhido = int(input("Escolha o número: "))
    
if numero_escolhido == numero_secreto:
    print(f"Acertou mizeravi, o número secreto é {numero_secreto}")

