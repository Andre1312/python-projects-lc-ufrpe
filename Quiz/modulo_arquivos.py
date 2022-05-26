
'''
UFRPE - Universidade Federal Rural de Pernambuco
DC - Departamento de Computação
Curso: Licenciatura Plena em Computação
Disciplina: Programação 1
Professor: Dr. João Paulo Lima
Aluno: André Luiz Coelho Barros

Projeto:
    Quiz Math


    Modulo Arquivos - funções para salvar CRUD  em aquivos .csv
'''
import csv


arquivo_quizmath = 'Quiz/quizmath.csv'
arquivo_top10 = 'Quiz/top10.csv'

def ler_arquivo_quizmath():
    lista_quizmath = ler_arquivo(arquivo_quizmath)
    return lista_quizmath

def salvar_arquivo_quizmath(quizmath):
    salvar_arquivo(arquivo_quizmath,quizmath)

def salvar_arquivo_inteiro_quizmath(quizmath):
    salvar_arquivo_inteiro(arquivo_quizmath,quizmath)

def ler_arquivo_top10():
    lista_top10 = ler_arquivo(arquivo_top10)
    return lista_top10

def salvar_arquivo_top10(top10):
    salvar_arquivo(arquivo_top10, top10)



# - funções básicas de ler e salvar arquivos .csv
def ler_arquivo(arquivo):
    with open(arquivo,'r', newline='') as arq:
        linhas = csv.reader(arq, delimiter=",")
        linhas = list(linhas)
    return linhas

def salvar_arquivo(arquivo,linha):
    with open(arquivo,'a',newline='') as arq:
        arq_csv = csv.writer(arq,delimiter=",")
        arq_csv.writerow(linha)

def salvar_arquivo_inteiro(arquivo,linhas):
    with open(arquivo,'w',newline='') as arq:
        arq_csv = csv.writer(arq,delimiter=",")
        arq_csv.writerows(linhas)