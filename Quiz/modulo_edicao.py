

'''
UFRPE - Universidade Federal Rural de Pernambuco
DC - Departamento de Computação
Curso: Licenciatura Plena em Computação
Disciplina: Programação 1
Professor: Dr. João Paulo Lima
Aluno: André Luiz Coelho Barros

Projeto:
    Quiz Math


    Modulo Edição - funções para CRUD no arquivo quizmath.csv
    
    campos:
        id
        dificuldade -> facil, medio, dificil
        pergunta -> facil: + e - | medio: +,- e x | dificil: +,-,x e /
        resposta_a
        resposta_b
        resposta_c
        resposta_correta -> resposta correta 'a', 'b' ou 'c'
    
'''      
    

import csv
import time
from prettytable import PrettyTable

import modulo_util as MUT
import modulo_arquivos as MA

def adicionarQuiz():
    quiz = []
    quizs = MA.ler_arquivo_quizmath()
    cabecalho = quizs[0]
    quizs.pop(0)
    print('ADICIONAR PERGUNTAS E RESPOSTAS')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()
    id_quiz = str(input('Entre com o ID da Pergunta (S sai...): ')).lower()
    if id_quiz in ['s']:
        MUT.limpaTela()
        return
        # testa se id é unico
    for linha in quizs:
        if id_quiz == linha[0]:
            print('Pergunta já existe ! Digite um novo ID único...')
            time.sleep(1.5)
            MUT.limpaTela()
            return
        
    dificuldade = str(input("Entre com a dificuldade F: 'facil', M: 'medio', D: 'dificil' : ")).lower()
    if dificuldade == 'f':
        dificuldade = 'facil'
    elif dificuldade == 'm':
        dificuldade = 'medio'
    elif dificuldade == 'd':
        dificuldade = 'dificil'
        
    pergunta = str(input('Entre com a pergunta matemática: '))
    resposta_a = str(input("Entre com a resposta para letra 'a.' : "))
    resposta_b = str(input("Entre com a resposta para letra 'b.' : "))
    resposta_c = str(input("Entre com a resposta para letra 'c.' : "))
    resposta_correta = str(input("Entre com a resposta correta 'a', 'b', 'c' : ")).lower()
          
    quiz.append(id_quiz)
    quiz.append(dificuldade)
    quiz.append(pergunta)
    quiz.append(resposta_a)
    quiz.append(resposta_b)
    quiz.append(resposta_c)
    quiz.append(resposta_correta)
       
    MA.salvar_arquivo_quizmath(quiz)

def editarQuiz():
    msg=0
    edicao_quiz = []
    quizs = MA.ler_arquivo_quizmath()
    cabecalho = quizs[0]
    quizs.pop(0)
    print('EDITAR PERGUNTAS E RESPOSTAS')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_quiz = str(input('Entre com o ID da pergunta (S sai...): ')).lower()
    if id_quiz in ['s']:
        return
    for linha in quizs:
        if id_quiz == linha[0]:
            idx = quizs.index(linha)
        else:
            msg+=1
    if msg == len(quizs):
        print('Pergunta Inexistente... entre com ID valido da lista de perguntas...')    
        print()
        while True:
            opcao = input('V para voltar... ').lower()
            if opcao in ['v']:
                break
        return
    
    edicao = PrettyTable()
    edicao.field_names=["ID","DIFICULDADE","PERGUNTA","RESPOSTA a.","RESPOSTA b.","RESPOSTA c.","RESPOSTA CORRETA"]
    edicao.add_row(quizs[idx])
    print(edicao)
    print()
    
    dificuldade = str(input("Entre com a dificuldade F: 'facil', M: 'medio', D: 'dificil' : ")).lower()
    if dificuldade == 'f':
        dificuldade = 'facil'
    elif dificuldade == 'm':
        dificuldade = 'medio'
    elif dificuldade == 'd':
        dificuldade = 'dificil'
        
    pergunta = str(input('Entre com a pergunta matemática: '))
    resposta_a = str(input("Entre com a resposta para letra 'a.' : "))
    resposta_b = str(input("Entre com a resposta para letra 'b.' : "))
    resposta_c = str(input("Entre com a resposta para letra 'c.' : "))
    resposta_correta = str(input("Entre com a resposta correta 'a', 'b', 'c' : ")).lower()
          
    edicao_quiz.append(id_quiz)
    edicao_quiz.append(dificuldade)
    edicao_quiz.append(pergunta)
    edicao_quiz.append(resposta_a)
    edicao_quiz.append(resposta_b)
    edicao_quiz.append(resposta_c)
    edicao_quiz.append(resposta_correta)
    
    quizs.remove(quizs[idx])
    quizs.insert(idx,edicao_quiz)
           
    quizs_ordenada = []
    quizs_ordenada = MUT.classificar_listas(quizs,0,'a')
    quizs_ordenada.insert(0,cabecalho)
       
    MA.salvar_arquivo_inteiro_quizmath(quizs_ordenada)
           
    return
        

def listarQuiz():
    print('LISTA DE PERGUNTAS E RESPOSTAS')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()
    quizs=MA.ler_arquivo_quizmath()
    cabecalho = quizs[0]
    quizs.pop(0)
    tabela = PrettyTable()
    tabela.field_names=["ID","DIFICULDADE","PERGUNTA","RESPOSTA a.","RESPOSTA b.","RESPOSTA c.","RESPOSTA CORRETA"]
        
    for linha in quizs:
        tabela.add_row(linha)
        
    print(tabela)
    print(f'Registros: {len(quizs)}')
    print()
    while True:
        opcao = input('V para voltar... ').lower()
        if opcao in ['v']:
            break

def apagarQuiz():
    msg=0
    edicao_quiz = []
    quizs = MA.ler_arquivo_quizmath()
    cabecalho = quizs[0]
    quizs.pop(0)
    print('APAGAR PERGUNTAS E RESPOSTAS')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_quiz = str(input('Entre com o ID da pergunta (S sai...): ')).lower()
    if id_quiz in ['s']:
        return
    for linha in quizs:
        if id_quiz == linha[0]:
            idx = quizs.index(linha)
        else:
            msg+=1
    if msg == len(quizs):
        print('Quiz Inexistente... entre com ID valido da lista de perguntas...')    
        print()
        while True:
            opcao = input('V para voltar... ').lower()
            if opcao in ['v']:
                break
        return
    
    edicao = PrettyTable()
    edicao.field_names=["ID","DIFICULDADE","PERGUNTA","RESPOSTA a.","RESPOSTA b.","RESPOSTA c.","RESPOSTA CORRETA"]
    edicao.add_row(quizs[idx])
    print(edicao)
    print()
    
    while True:         
        resposta = str(input('Apagar linha com ID de perguntas e respostas? S para SIM e N para NÃO : ')).lower()
        if resposta in ['s','n']:
            if resposta == 's':
                break
            elif resposta == 'n':
                return
               
    quizs.remove(quizs[idx])
     
    quizs_ordenada = []
    quizs_ordenada = MUT.classificar_listas(quizs,0,'a')
    quizs_ordenada.insert(0,cabecalho)
       
    MA.salvar_arquivo_inteiro_quizmath(quizs_ordenada)
    
    return

