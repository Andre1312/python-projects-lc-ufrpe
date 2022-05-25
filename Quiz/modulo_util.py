'''
UFRPE - Licenciatura em Computacao
Laboratorio de Programacao 1
Aluno - Andre Barros
PROJETO 2VA - Controle de Estoque

    Módulo utilidades

'''
import os
import time

import modulo_arquivos as MA



def limpar_tela():
# Função limpa tela do terminal
    os.system('cls' if os.name=='nt' else 'clear')

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
            print(f'{linha}')
            lista.append(linha)
    
    brk = input('break:>')
    time.sleep(1.0)
    limpar_tela()
    
    return lista

def mostrar_top10():
    print('TOP 10 - Jogadores')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()

    time.sleep(1.0)
    limpar_tela()

def editar_perguntas_respostas():
    print('Editar Perguntas e Respostas')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()

    time.sleep(1.0)
    limpar_tela()
    
