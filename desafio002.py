import random
aleatorio = random.randint(0, 10)
count = 0
while int(input("Tente acertar o numero! Digite: ")) != aleatorio:
    count += 1
print(f"Você acertou com {count} tentativa(s)! O valor era: {aleatorio}")