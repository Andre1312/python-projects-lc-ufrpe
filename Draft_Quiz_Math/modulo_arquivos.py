
import csv

# arquivo_quizmath = 'Quiz_Math/quizmath.csv'
# arquivo_top10 = 'Quiz_Math/top10.csv'

def ler_arquivo(arquivo):
    with open(arquivo,'r', newline='') as arq:
        linhas = csv.reader(arq, delimiter=",")
        linhas = list(linhas)
    return linhas

def salvar_arquivo(arquivo):
    with open(arquivo,'a',newline='') as arq:
        arq_csv = csv.writer(arq,delimiter=",")
        arq_csv.writerow(linha)

def salvar_arquivo_inteiro(arquivo):
    with open(arquivo,'w',newline='') as arq:
        arq_csv = csv.writer(arq,delimiter=",")
        arq_csv.writerows(linha)