sexo = str(input("Digite o seu sexo: "))
while(sexo.upper() != "M" and sexo.upper() != "F"):
    sexo = str(input("Invalido!! \nDigite o seu sexo: "))
print("Masculino" if sexo.upper() == "M" else "Feminino")