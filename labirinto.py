#by Larissa
def buscar_entrada(matriz):
    for n in range(len(matriz[0])):
        if matriz[0][n] == 1:
            return n  # Retorna o índice da entrada
    return -1  # Se não encontrar entrada, retorna -1

def buscar_vizinho(matriz, n):
    percorrido = []
    visitados = set()  # Usar um set para rastrear visitados
    caminho = []

    if n == -1:
        print("Nenhuma entrada encontrada!")
        return caminho

    try:
        r, c = 0, n  # Começa na entrada encontrada
        percorrido.append((r, c))
        visitados.add((r, c))
        caminho.append((r, c))

        while r < len(matriz) - 1:
            # Retrocede para a última posição no caminho
            r, c = caminho[-1]

            # Tenta mover para baixo, esquerda, direita, ou cima
            if r + 1 < len(matriz) and matriz[r + 1][c] == 1 and (r + 1, c) not in visitados:  # Desce
                r += 1
            elif c - 1 >= 0 and matriz[r][c - 1] == 1 and (r, c - 1) not in visitados:  # Esquerda
                c -= 1
            elif c + 1 < len(matriz[0]) and matriz[r][c + 1] == 1 and (r, c + 1) not in visitados:  # Direita
                c += 1
            elif r - 1 >= 0 and matriz[r - 1][c] == 1 and (r - 1, c) not in visitados:  # Cima
                r -= 1
            else:  # Se não há mais vizinhos válidos, retrocede
                caminho.pop()
                if not caminho:  # Se o caminho estiver vazio, significa que não há caminho
                    break
                continue  # Repetir o loop para retroceder

            # Adiciona a nova posição ao caminho
            percorrido.append((r, c))
            visitados.add((r, c))
            caminho.append((r, c))

            # Verifica se chegou ao final do labirinto
            if r == len(matriz) - 1:
                break

        print("\nCaminho ->", caminho)
        return caminho

    except Exception as e:
        print("Erro ao executar o código:", e)
        return []

def imprimir_labirinto(matriz, caminho):
    for r in range(len(matriz)):
        for c in range(len(matriz[0])):
            if (r, c) in caminho:
                print(1, end=" ")  # Exibe '1' para o caminho encontrado
            else:
                print(matriz[r][c], end=" ")  # Exibe o valor original
        print()  # Nova linha após cada linha do labirinto

# Labirinto de exemplo
labirinto = [
    [0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]
]


n = buscar_entrada(labirinto)
caminho = buscar_vizinho(labirinto, n)
imprimir_labirinto(labirinto, caminho)
