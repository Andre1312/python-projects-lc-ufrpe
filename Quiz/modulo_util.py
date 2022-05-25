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
    if dificuldade == 'facil':
        print('Jogo com dificuldade FACIL')
        
        # chama função carrega perguntas e respostas nivel fácil 
        # retorna lista de perguntas e respostas nivel facil do arquivo quizmath.csv
        lista_perguntas_respostas = MA.ler_arquivo_quizmath()
        for linha in lista_perguntas_respostas:
            #retira da lista perguntas nivel medio e dificil
            if linha[1] == 'medio' or linha[1] == 'dificil':
                idx = lista_perguntas_respostas.index(linha[1])
                lista_perguntas_respostas.pop(idx)
            print(linha)
               
        time.sleep(1.0)
        limpar_tela()

        # lista_perguntas_respostas = ler_perguntas_respostas(dificuldade)
        # lista_perguntas_respostas = []
        return lista_perguntas_respostas

    elif dificuldade == 'medio':
        print('Jogo com dificuldade MEDIO')
        
        # chama função carrega perguntas e respostas nivel medio 
        # retorna lista de perguntas e respostas nivel facil do arquivo quizmath.csv
        lista_perguntas_respostas = MA.ler_arquivo_quizmath()
        for linha in lista_perguntas_respostas:
            #retira da lista perguntas nivel facil e dificil
            if 'facil' in linha:
                idx = lista_perguntas_respostas.index('facil')
                print(f'idx-{idx}')
                lista_perguntas_respostas.pop(idx)
            print(linha)
               
        b = input('break:>')
        limpar_tela()

        # lista_perguntas_respostas = ler_perguntas_respostas(dificuldade)
        # lista_perguntas_respostas = []
        return lista_perguntas_respostas

    elif dificuldade == 'dificil':
        print('Jogo com dificuldade DIFICIL')
        
        # chama função carrega perguntas e respostas nivel dificil 
        # retorna lista de perguntas e respostas nivel facil do arquivo quizmath.csv
        lista_perguntas_respostas = MA.ler_arquivo_quizmath()
        for linha in lista_perguntas_respostas:
            #retira da lista perguntas nivel medio e facil
            if linha[1] == 'medio' or linha[6] == 'facil':
                idx = lista_perguntas_respostas.index(linha[1])
                lista_perguntas_respostas.pop(idx)
            print(linha)
               
        time.sleep(1.0)
        limpar_tela()

        # lista_perguntas_respostas = ler_perguntas_respostas(dificuldade)
        # lista_perguntas_respostas = []
        return lista_perguntas_respostas

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
    
