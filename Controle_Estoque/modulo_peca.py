'''
UFRPE - Licenciatura em Computacao
Laboratorio de Programacao 1
Aluno - Andre Barros
PROJETO 2VA - Controle de Estoque



    Modulo peça - funções para CRUD no arquivo peca.csv
    
    campos:
    id_peca
    nome
    tipo
    data_atualizacao
    ativo
'''      
    

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
    msg=0
    edicao_peca = []
    pecas = lerPeca()
    print('EDITAR PEÇA')
    print('¬¬¬¬¬¬¬¬¬¬¬')
    id_peca = str(input('Entre com o ID da peça (S sai...): ')).lower()
    if id_peca in ['s']:
        return
    for u in pecas:
        if id_peca in u[0]:
            idx = pecas.index(u)
        else:
            msg+=1
    if msg == len(pecas):
        print('Peça Inexistente... entre com ID valido da lista de peças...')    
        print()
        while True:
            opcao = input('V para voltar... ').lower()
            if opcao in ['v']:
                break
        return
    
    edicao = PrettyTable()
    edicao.field_names=["ID","NOME","TIPO","DATA","ATIVO"]
    edicao.add_row(pecas[idx])
    print(edicao)
    print()
    
    nome = str(input('Entre com o NOME da peça: ')).title()
    tipo = str(input('Entre com o TIPO da peca: ')).upper()
    data_atualizacao = datetime.datetime.now()
    data_atualizacao = data_atualizacao.strftime("%Y/%m/%d %H:%M:%S")
    ativo = str(input('S para ativo e N para desativado: ')).lower()
    
    edicao_peca.append(id_peca)
    edicao_peca.append(nome)
    edicao_peca.append(tipo)
    edicao_peca.append(data_atualizacao)
    edicao_peca.append(ativo)
    
    pecas.remove(pecas[idx])
    pecas.append(edicao_peca)
       
    salvarPecaArquivo(pecas)
    
    return
        

def listarPeca():
    print('LISTA DE PEÇAS')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()
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
    msg=0
    edicao_peca = []
    pecas = lerPeca()
    print('APAGAR PEÇA')
    print('¬¬¬¬¬¬¬¬¬¬¬')
    id_peca = str(input('Entre com o ID da peça (S sai...): ')).lower()
    if id_peca in ['s']:
        return
    for u in pecas:
        if id_peca in u[0]:
            idx = pecas.index(u)
        else:
            msg+=1
    if msg == len(pecas):
        print('Peca Inexistente... entre com ID valido da lista de peças...')    
        print()
        while True:
            opcao = input('V para voltar... ').lower()
            if opcao in ['v']:
                break
        return
    
    edicao = PrettyTable()
    edicao.field_names=["ID","NOME","TIPO","DATA","ATIVO"]
    edicao.add_row(pecas[idx])
    print(edicao)
    print()
    
    id_peca = pecas[idx][0]
    nome = pecas[idx][1]
    tipo = pecas[idx][2]
    data_atualizacao = pecas[idx][3]
        
    ativo = str(input('S para ativo e N para desativado: ')).lower()
    
    edicao_peca.append(id_peca)
    edicao_peca.append(nome)
    edicao_peca.append(tipo)
    edicao_peca.append(data_atualizacao)
    edicao_peca.append(ativo)
    
    pecas.remove(pecas[idx])
    pecas.append(edicao_peca)
       
    salvarPecaArquivo(pecas)

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

def salvarPecaArquivo(peca):
    arquivo = 'Controle_Estoque/peca.csv'
    with open(arquivo,'w',newline='') as arq:
        arq_csv = csv.writer(arq,delimiter=",")
        arq_csv.writerows(peca)