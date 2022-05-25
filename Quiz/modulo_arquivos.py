
import csv

arquivo_quizmath = 'Quiz_Math/quizmath.csv'
arquivo_top10 = 'Quiz_Math/top10.csv'

def ler_arquivo_quizmath():
    lista_quizmath = ler_arquivo(arquivo_quizmath)
    return lista_quizmath

def ler_arquivo_top10():
    lista_top10 = ler_arquivo(arquivo_top10)
    return lista_top10

def salvar_arquivo_top10(top10):
    salvar_arquivo(arquivo_top10, top10)

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