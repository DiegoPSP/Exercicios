def expo(N, B, K):
    # Inicializa os valores de B e K
    B[0] = 1
    K[0] = 0

    # Encontrar o menor B tal que B^k = N
    while B[0] <= N:
        if N % B[0] == 0:
            aux = N // B[0]
            auxK = 0

            # Verifica se B^k = N
            while aux % B[0] == 0:
                aux //= B[0]
                auxK += 1

            # Se sim, atualiza os valores de B e K
            if aux == 1 and auxK > 0:
                K[0] = auxK
                break

        B[0] += 1

N = 27
B = [0]  # Lista para simular passagem por referência
K = [0]  # Lista para simular passagem por referência

expo(N, B, K)

print(f"Para N = {N}, o menor B é {B[0]} e K é {K[0]}.")
