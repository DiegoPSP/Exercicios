sexo = str(input("Digite seu sexo com apenas uma letra: "))
while sexo.upper() != "M" and sexo.upper() != "F":
    sexo = str(input("Inválido! Tente novamente: "))
print("Masculino" if sexo.upper() == "M"  else "Feminino!")