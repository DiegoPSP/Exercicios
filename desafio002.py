import random
aleatorio = random.randint(0, 10)
valor = int(input("Tente acertar o numero! Digite: "))
while valor != aleatorio:
    valor = int(input("Errado! Tente novamente: "))
print("Você acertou!", aleatorio)