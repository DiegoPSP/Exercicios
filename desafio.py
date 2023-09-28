while True:
    sexo = str(input("Digite seu sexo com apenas uma letra: "))
    if sexo.upper() == "M":
        print("Seu sexo é masculino, você é cabra macho!")
        exit()
    elif sexo.upper() == "F":
        print("Seu sexo é feminino, você é uma princesa!")
        exit()
    else:
        print("Não foi possível reconhecer seu sexo, por favor tente novamente.")
