def buscar_entrada (matriz):
    n = 0
    try:
        while n < len(matriz[0]):
            if matriz[0][n] == 1 :
                indice_inicio = matriz[0][n]
                return n
            else: 
                n+=1
    except:
        print("Erro ao executar o While")

def buscar_vizinho (matriz, n):
    percorrido = []
    visitados = []
    caminho = []

    try:
        r = 0
        c = n
        indice_inicio = matriz[r][c]
        percorrido.append((r,c))
        visitados.append((r,c))
        caminho.append((r,c))


        while r < len(matriz) - 1 :
            r, c = caminho[-1] # retrocesso
            
            if r + 1 < len(matriz) and matriz[r+1][c] == 1 and (r + 1, c) not in visitados: # desce
                r+=1 # movimento
                percorrido.append((r,c))
                visitados.append((r,c))
                caminho.append((r,c))
            elif c - 1 < len(matriz) and matriz[r][c-1] == 1 and (r, c - 1) not in visitados: # esquerda
                c-=1 # movimento
                percorrido.append( (r,c))
                visitados.append((r,c))
                caminho.append((r,c))
            elif c + 1 < len(matriz) and matriz[r][c+1] == 1 and (r, c + 1) not in visitados: # direita
                c+=1 # movimento
                percorrido.append((r,c))
                visitados.append((r,c))
                caminho.append((r,c))
            elif r - 1 < len(matriz) and matriz[r-1][c] == 1 and (r - 1, c) not in visitados: # sobe
                r-=1 # movimento
                percorrido.append((r,c))
                visitados.append((r,c))
                caminho.append((r,c))
            else: 
                caminho.pop() #retrocesso
            if r == len(matriz) - 1 :
                break

        print("\nCaminho ->  ", caminho)
        return caminho
  
    except Exception as e:
        print("Erro ao executar o código : ", e)

def imprimir_labirinto (matriz,caminho): #by chatgpt

    def colorir_texto(texto, cor): 
        cores = {
            'verde': '\033[92m',  # Verde
            'reset': '\033[0m',   # Resetar cor
        }
   
        return f"{cores[cor]}{texto}{cores['reset']}"

    for r in range(len(matriz)):
        print("\n")
        for c in range(len(matriz[0])):
            if (r, c) in caminho:
                print(colorir_texto(matriz[r][c], 'verde'), end=" ")
            else:
                print(matriz[r][c], end=" ")
    print()

labirinto = [
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0]
]

n = buscar_entrada(labirinto)
caminho = buscar_vizinho(labirinto, n)
imprimir_labirinto(labirinto, caminho)
