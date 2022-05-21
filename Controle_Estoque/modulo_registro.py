'''
UFRPE - Licenciatura em Computacao
Laboratorio de Programacao 1
Aluno - Andre Barros
PROJETO 2VA - Controle de Estoque



    Modulo registro - funções para CRUD no arquivo registro.csv
    
    campos:
    id_registro
    id_usuario
    id_peca
    qtde_inicial
    qtde_adicionada
    qtde_removida
    data_atualizacao
    ativo
    
'''      
    

import csv
import time
import datetime
from prettytable import PrettyTable

import modulo_util as MUT

def adicionarEstoque():
    registro = []
    registros = lerEstoque()
    print('ADICIONAR REGISTRO AO ESTOQUE')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_registro = str(input('Entre com o ID de registro (S sai...): ')).lower()
    if id_registro in ['s']:
        return
        # testa se id_registro é unico
    for linha in registros:
        if id_registro == linha[0]:
            print('Registro já existe ! Digite um novo ID...')
            time.sleep(1)
            MUT.limpaTela()
            return
    
    id_usuario = str(input('Entre com o ID Usuario do registro: ')).title()
    id_peca = str(input('Entre com o ID Peça do registro: ')).upper()
    qtde_inicial = str(int(input('Entre com a Quantidade inicial: ')))
    qtde_adicionada = str(int(input('Entre com a Quantidade adicionada: ')))
    qtde_removida = str(int(input('Entre com a Quantidade removida: ')))
    data_atualizacao = datetime.datetime.now()
    data_atualizacao = data_atualizacao.strftime("%Y/%m/%d %H:%M:%S")
    ativo = 's'
    
    registro.append(id_registro)
    registro.append(id_usuario)
    registro.append(id_peca)
    registro.append(qtde_inicial)
    registro.append(qtde_adicionada)
    registro.append(qtde_removida)
    registro.append(data_atualizacao)
    registro.append(ativo)
    
    salvarEstoque(registro)

def editarEstoque():
    msg=0
    edicao_registro = []
    registros = lerEstoque()
    print('EDITAR REGISTRO ESTOQUE')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_registro = str(input('Entre com o ID da registro (S sai...): ')).lower()
    if id_registro in ['s']:
        return
    for u in registros:
        if id_registro in u[0]:
            idx = registros.index(u)
        else:
            msg+=1
    if msg == len(registros):
        print('Registro Inexistente... entre com ID valido da lista de peças...')    
        print()
        while True:
            opcao = input('V para voltar... ').lower()
            if opcao in ['v']:
                break
        return
    
    edicao = PrettyTable()
    edicao.field_names=["ID","ID_USUARIO","ID_PEÇA","QTDE_INICIAL","QTDE ADICIONADA","QTDE REMOVIDA","DATA","ATIVO"]
    edicao.add_row(registros[idx])
    print(edicao)
    print()
    
    id_usuario = str(input('Entre com o ID Usuario do registro: ')).title()
    id_peca = str(input('Entre com o ID Peça do registro: ')).upper()
    qtde_inicial = str(int(input('Entre com a Quantidade inicial: ')))
    qtde_adicionada = str(int(input('Entre com a Quantidade adicionada: ')))
    qtde_removida = str(int(input('Entre com a Quantidade removida: ')))
    data_atualizacao = datetime.datetime.now()
    data_atualizacao = data_atualizacao.strftime("%Y/%m/%d %H:%M:%S")  
        
    ativo = str(input('S para ativo e N para desativado: ')).lower()
    
    edicao_registro.append(id_registro)
    edicao_registro.append(id_usuario)
    edicao_registro.append(id_peca)
    edicao_registro.append(qtde_inicial)
    edicao_registro.append(qtde_adicionada)
    edicao_registro.append(qtde_removida)
    edicao_registro.append(data_atualizacao)
    edicao_registro.append(ativo)
    
    registros.remove(registros[idx])
    registros.append(edicao_registro)
       
    salvarEstoqueArquivo(registros)

def listarEstoque():
    print('LISTA DE ESTOQUE')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()
    registros=lerEstoque()
    tabela = PrettyTable()
    tabela.field_names=["ID","ID_USUARIO","ID_PEÇA","QTDE_INICIAL","QTDE ADICIONADA","QTDE REMOVIDA","DATA","ATIVO"]
        
    for r in registros:
        tabela.add_row(r)
        
    print(tabela)
    print(f'Registros: {len(registros)}')
    print()
    while True:
        opcao = input('V para voltar... ').lower()
        if opcao in ['v']:
            break

def apagarEstoque():
    msg=0
    edicao_registro = []
    registros = lerEstoque()
    print('APAGAR REGISTRO ESTOQUE')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_registro = str(input('Entre com o ID da registro (S sai...): ')).lower()
    if id_registro in ['s']:
        return
    for u in registros:
        if id_registro in u[0]:
            idx = registros.index(u)
        else:
            msg+=1
    if msg == len(registros):
        print('Registro Inexistente... entre com ID valido da lista de peças...')    
        print()
        while True:
            opcao = input('V para voltar... ').lower()
            if opcao in ['v']:
                break
        return
    
    edicao = PrettyTable()
    edicao.field_names=["ID","ID_USUARIO","ID_PEÇA","QTDE_INICIAL","QTDE ADICIONADA","QTDE REMOVIDA","DATA","ATIVO"]
    edicao.add_row(registros[idx])
    print(edicao)
    print()
    
    id_registro = registros[idx][0]
    id_usuario = registros[idx][1]
    id_peca = registros[idx][2]
    qtde_inicial = registros[idx][3]
    qtde_adicionada = registros[idx][4]
    qtde_removida = registros[idx][5]
    data_atualizacao = datetime.datetime.now()
    data_atualizacao = data_atualizacao.strftime("%Y/%m/%d %H:%M:%S")  
        
    ativo = str(input('S para ativo e N para desativado: ')).lower()
    
    edicao_registro.append(id_registro)
    edicao_registro.append(id_usuario)
    edicao_registro.append(id_peca)
    edicao_registro.append(qtde_inicial)
    edicao_registro.append(qtde_adicionada)
    edicao_registro.append(qtde_removida)
    edicao_registro.append(data_atualizacao)
    edicao_registro.append(ativo)
    
    registros.remove(registros[idx])
    registros.append(edicao_registro)
       
    salvarEstoqueArquivo(registros)

def salvarEstoque(registro):
    arquivo = 'Controle_Estoque/registro.csv'
    with open(arquivo,'a',newline='') as arq:
        arq_csv=csv.writer(arq,delimiter=",")
        arq_csv.writerow(registro)

def lerEstoque():
    arquivo = 'Controle_Estoque/registro.csv'
    with open(arquivo,'r',newline='') as arq:
        registros = csv.reader(arq, delimiter=",")
        registros = list(registros)
    return registros

def salvarEstoqueArquivo(registro):
    arquivo = 'Controle_Estoque/registro.csv'
    with open(arquivo,'w',newline='') as arq:
        arq_csv = csv.writer(arq,delimiter=",")
        arq_csv.writerows(registro)