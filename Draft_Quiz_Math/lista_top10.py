import os
import csv


def ler_arquivo(arquivo):
    with open(arquivo,'r', newline='') as arq:
        linhas = csv.reader(arq, delimiter=",")
        linhas = list(linhas)
    return linhas

def trocar_listas(lista_a, lista_b):
    # print(f'O {lista_a} <<>> {lista_b}')
    lista_a, lista_b = lista_b, lista_a
    lista_troca = []
    lista_troca.append(lista_a)
    lista_troca.append(lista_b)
    # print(f'T {lista_troca[0]} <<>> {lista_troca[1]}')
    return lista_troca

def classificar_listas(lista, posicao, ordem):
    '''
    Função para classificar listas
        lista -> lista que se quer ordenar com cabeçalho
        posicao -> index do campo numerico que se quer ordenar
        ordem = 'A' << Ascedente
        ordem = 'D' >> Descendente
        
        return lista
    '''
    lista_trocada = []
    lista_ordenada = []
    for i in range(len(lista)):
        if i == 0:
            continue
        for j in range(len(lista)):
            if j ==  0:
                continue
            if ordem == 'a' or ordem == 'A':
                if int(lista[i][posicao]) <= int(lista[j][posicao]):
                    lista_trocada = trocar_listas(lista[i],lista[j])
                    lista[i] = lista_trocada[0]
                    lista[j] = lista_trocada[1]
            elif ordem == 'd' or ordem == 'D':
                if int(lista[i][posicao]) >= int(lista[j][posicao]):
                    lista_trocada = trocar_listas(lista[i],lista[j])
                    lista[i] = lista_trocada[0]
                    lista[j] = lista_trocada[1]
            # print()
            # print(f'LO {i}:{lista[i]} L {j}:{lista[j]}')
            # print(f'LT {i}:{lista_trocada[0]} LT {j} {lista_trocada[1]}')
        

    lista_ordenada = lista
    # print()    
    return lista_ordenada



arquivo = 'Draft_Quiz_Math/lista_top10.txt'
lista_top10 = ler_arquivo(arquivo)

os.system('cls')

for l in lista_top10:
    print (l)
print('¬' * 40)

lista_ordenada = classificar_listas(lista_top10,1,'d')

print()
for lo in (lista_ordenada):
    print(lo)
print('¬' * 40)




