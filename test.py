# Definindo o labirinto
labirinto = [
    [0, 8, 0],
    [4, 5, 6],
    [0, 2, 0]
]

# Posição [1,1] onde está o '5'
posicao_x = 1
posicao_y = 1

# Função para verificar os quatro cantos ao redor de [1,1]
def verificar_zeros_ao_redor(labirinto, x, y):
    direcoes = [
        (-1, 0),  # acima
        (1, 0),   # abaixo
        (0, -1),  # à esquerda
        (0, 1)    # à direita
    ]
    
    zeros_ao_redor = []
    
    for dx, dy in direcoes:
        novo_x = x + dx
        novo_y = y + dy
        
        # Verifica se está dentro dos limites do labirinto
        if 0 <= novo_x < len(labirinto) and 0 <= novo_y < len(labirinto[0]):
            if labirinto[novo_x][novo_y] == 0:
                zeros_ao_redor.append((novo_x, novo_y))
    
    return zeros_ao_redor

# Verificando se há zeros ao redor da posição [1,1]
zeros_encontrados = verificar_zeros_ao_redor(labirinto, posicao_x, posicao_y)

# Exibindo os resultados
if zeros_encontrados:
    print("Zeros encontrados nas posições:", zeros_encontrados)
else:
    print("Nenhum zero encontrado ao redor de [1,1]")
