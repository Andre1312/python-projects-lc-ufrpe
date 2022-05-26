

'''
UFRPE - Universidade Federal Rural de Pernambuco
DC - Departamento de Computação
Curso: Licenciatura Plena em Computação
Disciplina: Programação 1
Professor: Dr. João Paulo Lima
Aluno: André Luiz Coelho Barros

Projeto:
    Quiz Math

Módulo Útil

'''
import os
import time

import modulo_arquivos as MA
import modulo_edicao as ME

TEMPO_ESPERA = 1.0

def limpar_tela():
# Função limpa tela do terminal
    os.system('cls' if os.name=='nt' else 'clear')
    
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

def preparar_jogo(dificuldade):
    
    lista=[]
    
    if dificuldade == 'facil':
        print('Jogo com dificuldade nivel FACIL')
    elif dificuldade == 'medio':
        print('Jogo com dificuldade nivel MEDIO')
    elif dificuldade == 'dificil':
        print('Jogo com dificuldade nivel DIFICIL')   
        
    # chama função carrega perguntas e respostas nivel fácil 
    # retorna lista de perguntas e respostas nivel facil do arquivo quizmath.csv
    lista_perguntas_respostas = MA.ler_arquivo_quizmath()
    for linha in lista_perguntas_respostas:
        #retira da lista perguntas nivel facil, medio e dificil de acordo com a variavel dificuldade
        if linha[0] == 'id':
            continue
        if linha[1] == dificuldade:
            # print(f'{linha}')
            lista.append(linha)
    
    # brk = input('break:>')
    time.sleep(1.0)
    limpar_tela()
    
    return lista

def mostrar_top10(lista):
    
    lista_ordenada = classificar_listas(lista, 1, 'D')
    limpar_tela()
    print('TOP 10 - Jogadores')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()
    lista_ordenada.pop(0)
    i=0
    dificuldade = str(input("Digite 'F' para Fácil, 'M' para Médio, 'D' para Difícil e 'L' para lista geral: ")).lower()
    print()
    if dificuldade == 'f':
        i = 0
        for l in lista_ordenada:
            if l[2] == 'facil':
                print(f'\t{i+1}. {l[0]} : {l[1]} : Facil')
                i+=1       
    elif dificuldade == 'm':
        i = 0
        for l in lista_ordenada:
            if l[2] == 'medio':
                print(f'\t{i+1}. {l[0]} : {l[1]} : Medio')
                i+=1        
    elif dificuldade == 'd':
        i = 0
        for l in lista_ordenada:
            if l[2] == 'dificil':
                print(f'\t{i+1}. {l[0]} : {l[1]} : Dificil')
                i+=1
    elif dificuldade == 'l':
        i = 0
        for l in lista_ordenada:
            if i < 10:
                print(f'\t{i+1}. {l[0]} : {l[1]} : {l[2]}')
            i+=1                 
    print()
    while True:
        resposta = str(input('Digite V para voltar ao Menu Principal...')).lower()
        if resposta == 'v':
            break    
    return  
    

def editar_perguntas_respostas():
    limpar_tela()
    print('Editar Perguntas e Respostas')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()
    print('1 - Adicionar Perguntas e Respostas')
    print('2 - Editar Perguntas e Respostas')
    print('3 - Listar Perguntas e Respostas')
    print('4 - Apagar Perguntas e Respostas')
    print('V - Voltar ao MENU PRINCIPAL')
    print()
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1', '2', '3', '4', 'v']:
            break
        limpar_tela()
        editar_perguntas_respostas()
    if opcao == '1':
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        limpar_tela()
        ME.adicionarQuiz()
    elif opcao == '2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        limpar_tela()        
        ME.editarQuiz()
    elif opcao == '3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        limpar_tela()
        ME.listarQuiz()
    elif opcao == '4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        limpar_tela()
        ME.apagarQuiz()
    elif opcao == 'v':
        print('Selecionado V...')
        time.sleep(TEMPO_ESPERA)
        return

    time.sleep(1.0)
    limpar_tela()
    
