# Inicializa valores como uma lista vazia
valores = []

# Loop para receber números do usuário
while True:
    numero = input("Digite um número (ou digite 'exit' para encerrar): ")
    # Verifica se o usuário quer encerrar
    if numero.lower() == 'exit':
        break
    
    # Adiciona o número à lista
    valores.append(int(numero))

print("\nLista antes de ser ordenada:", valores)

# Implementação do algoritmo de ordenação (Bubble Sort)
n = len(valores)
for i in range(n):
    for j in range(0, n - i - 1):
        if valores[j] > valores[j + 1]:
            valores[j], valores[j + 1] = valores[j + 1], valores[j]

# Exibe a lista ordenada
print("\nLista ordenada:", valores)
