lb = [[0, 0, 1, 0, 0, 0],
      [0, 1, 1, 0, 1, 0],
      [0, 1, 0, 0, 1, 0],
      [0, 1, 1, 1, 1, 0],
      [0, 0, 0, 1, 0, 0],
      [0, 1, 1, 1, 0, 0],
      [0, 1, 0, 1, 1, 0],
      [0, 1, 0, 0, 0, 0]]

def valor_labirinto(lista_desafio):
    encontrou_um = False
    for i in range(len(lista_desafio)):
        if lista_desafio[i] == 1:
            if not encontrou_um:
                encontrou_um = True 
            else:
                lista_desafio[i] = 0 
    return lista_desafio

for lista in lb:
    print(valor_labirinto(lista))
