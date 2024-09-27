lb = [
    [0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]]

'''
def valor_labirinto(lista_desafio):
    encontrou_um = False
    encontrou_zero = False
    for i in range(len(lista_desafio)):
        if lista_desafio[i] == 1 and not encontrou_zero:
            encontrou_um = True  
        elif lista_desafio[i] == 0 and encontrou_um:
            encontrou_zero = True  
        elif lista_desafio[i] == 1 and encontrou_zero:
            lista_desafio[i] = 0  
    return lista_desafio
'''

def index_lb():
    for chave in lb:
        for i, n  in enumerate(chave):
            print(f'{i, n}\n')

    

index_lb()

