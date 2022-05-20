"""
    Modulo peça - funções para CRUD no arquivo peca.csv
    
    campos:
    id_peca
    nome
    tipo
    data_atualizacao
    ativo
      
    
"""
import csv
import time
import datetime
from prettytable import PrettyTable

import modulo_util as MUT

def adicionarPeca():
    peca = []
    pecas = lerPeca()
    print('ADICIONAR PEÇA')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_peca = str(input('Entre com o ID da peça (S sai...): ')).lower()
    if id_peca in ['s']:
        return
        # testa se id_peca é unico
    for linha in pecas:
        if id_peca == linha[0]:
            print('Peça já existe ! Digite um novo ID...')
            time.sleep(1)
            MUT.limpaTela()
            adicionarPeca()
    peca.append(id_peca)
    nome = str(input('Entre com o NOME da peca: ')).title()
    tipo = str(input('Entre com o TIPO da peca: ')).upper()
    data_atualizacao = datetime.datetime.now()
    data_atualizacao = data_atualizacao.strftime("%Y/%m/%d %H:%M:%S")
    ativo = 's'
    peca.append(nome)
    peca.append(tipo) 
    peca.append(data_atualizacao)
    peca.append(ativo)
    
    salvarPeca(peca)

def editarPeca():
    pass

def listarPeca():
    pecas=lerPeca()
    tabela = PrettyTable()
    tabela.field_names=["ID","NOME","TIPO","DATA","ATIVO"]
        
    for u in pecas:
        tabela.add_row(u)
        
    print(tabela)
    print(f'Registros: {len(pecas)}')
    print()
    while True:
        opcao = input('V para voltar... ').lower()
        if opcao in ['v']:
            break

def apagarPeca():
    pass


def salvarPeca(peca):
    arquivo = 'Controle_Estoque/peca.csv'
    with open(arquivo,'a',newline='') as arq:
        arq_csv=csv.writer(arq,delimiter=",")
        arq_csv.writerow(peca)

def lerPeca():
    arquivo = 'Controle_Estoque/peca.csv'
    with open(arquivo,'r',newline='') as arq:
        pecas = csv.reader(arq, delimiter=",")
        pecas = list(pecas)
    return pecas