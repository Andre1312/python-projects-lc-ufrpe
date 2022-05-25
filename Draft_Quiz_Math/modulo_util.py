'''
UFRPE - Licenciatura em Computacao
Laboratorio de Programacao 1
Aluno - Andre Barros
PROJETO 2VA - Controle de Estoque

    Módulo utilidades

'''
import os
import time



def limpar_tela():
# Função limpa tela do terminal
    os.system('cls' if os.name=='nt' else 'clear')

def preparar_jogo(dificuldade):
    if dificuldade == 'facil':
        print('Jogo com dificuldade FACIL')
        # chama função carrega perguntas e respostas nivel fácil 
        # retorna lista de perguntas e respostas nivel facil do arquivo quizmath.csv
        time.sleep(1.0)
        limpar_tela()

        # lista_perguntas_respostas = ler_perguntas_respostas(dificuldade)
        lista_perguntas_respostas = []
        return lista_perguntas_respostas

    elif dificuldade == 'medio':
        print('Jogo com dificuldade MEDIO')
        # chama função carrega perguntas e respostas nivel médio 
        # retorna lista de perguntas e respostas nivel médio do aruivo
        time.sleep(1.0)
        limpar_tela()

        # lista_perguntas_respostas = ler_perguntas_respostas(dificuldade)
        lista_perguntas_respostas = []
        return lista_perguntas_respostas

    elif dificuldade == 'dificil':
        print('Jogo com dificuldade DIFICIL')
        # chama função carrega perguntas e respostas nivel dificil 
        # retorna lista de perguntas e respostas nivel dificil do arquivo quizmath.csv
        time.sleep(1.0)
        limpar_tela()

        # lista_perguntas_respostas = ler_perguntas_respostas(dificuldade)
        lista_perguntas_respostas = []
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
    
