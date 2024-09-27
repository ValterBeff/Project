labirinto = [
    [0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0]
]

visitado = []  # Lista para registrar coordenadas já visitadas
caminho = []   # Lista para armazenar o caminho

def dfs(x, y):
    # Verifica se a posição está fora dos limites ou já foi visitada
    if (x < 0 or x >= len(labirinto) or y < 0 or y >= len(labirinto[0]) or 
        labirinto[x][y] == 0 or (x, y) in visitado):
        return False
    
    # Marca a posição como visitada
    visitado.append((x, y))
    caminho.append((x, y))  # Adiciona ao caminho

    # Se chegar ao novo destino (7, 1)
    if (x == 7 and y == 1):
        return True
    
    # Chama a função recursivamente para vizinhos
    if (dfs(x + 1, y) or  # Abaixo
        dfs(x - 1, y) or  # Acima
        dfs(x, y + 1) or  # Direita
        dfs(x, y - 1)):   # Esquerda
        return True

    # Se não encontrou um caminho, remove do caminho
    caminho.pop()  # Remove a posição do caminho
    return False

def buscar_caminho():
    # Inicia a busca a partir da posição inicial (0, 2)
    if dfs(0, 2):  # Começa a busca da posição (0, 2)
        exibir_caminho()
    else:
        print("Nenhum caminho encontrado.")

def exibir_caminho():
    # Cria uma matriz vazia preenchida com zeros
    matriz_resultado = [[0 for _ in range(len(labirinto[0]))] for _ in range(len(labirinto))]
    
    # Preenche a matriz com o caminho encontrado
    for x, y in caminho:
        matriz_resultado[x][y] = 1  # Define o caminho com 1
    
    # Exibe a matriz resultante
    for linha in matriz_resultado:
        print(linha)

# Chama a função para buscar o caminho
buscar_caminho()
