import random
aleatorio = random.randint(0, 10)
count = 0
valor = int(input("Tente acertar o numero! Digite: "))
while valor != aleatorio:
    valor = int(input("Errado! Tente novamente: "))
    count += 1
print("Você acertou", count,"com tentativa(s)! O valor era:", aleatorio)