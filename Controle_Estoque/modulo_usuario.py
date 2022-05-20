"""
    Modulo usuario - funções para CRUD no arquivo usuario.csv

    campos:
    id_usuario
    nome
    sobrenome
    apelido
    data_atualizacao
    ativo
    

"""
import os
import csv
import time
import datetime
from prettytable import PrettyTable

import modulo_util as MUT

def adicionarUsuario():
    usuario = []
    usuarios = lerUsuario()
    print('ADICIONAR USUARIO')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_usuario = str(input('Entre com o ID do usuario (S sai...): ')).lower()
    if id_usuario in ['s']:
        return
        # testa se id_usuario é unico
    for linha in usuarios:
        if id_usuario in linha[0]:
            print('Usuario já existe ! Digite um novo ID...')
            time.sleep(1)
            MUT.limpaTela()
            adicionarUsuario()
    usuario.append(id_usuario)
    nome = str(input('Entre com o NOME do usuario: ')).title()
    sobrenome = str(input('Entre com o SOBRENOME do usuario: ')).title()
    apelido = str(input('Entre com o APELIDO do usuario: ')).upper()
    data_atualizacao = datetime.datetime.now()
    data_atualizacao = data_atualizacao.strftime("%Y/%m/%d %H:%M:%S")
    ativo = 's'
    usuario.append(nome)
    usuario.append(sobrenome) 
    usuario.append(apelido)
    usuario.append(data_atualizacao)
    usuario.append(ativo)
    
    salvarUsuario(usuario)
            
    

def editarUsuario():
    usuario = []
    usuarios = lerUsuario()
    print('EDITAR USUARIO')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_usuario = str(input('Entre com o ID do usuario (S sai...): ')).lower()
    if id_usuario in ['s']:
        return
    for u in usuarios:
        if id_usuario in u[0]:
            print(f'ID ::{u[0]} :: {u[3]} :: {u[1]}')
        elif id_usuario not in u[0]:
            print('Usuario Inexistente... entre com ID valido da lista de usuarios...')
        
    print()
    while True:
        opcao = input('V para voltar... ').lower()
        if opcao in ['v']:
            break  
    
        
def listarUsuario():
    usuarios = lerUsuario()
    tabela = PrettyTable()
    # tabela.clear()
    tabela.field_names=["ID","NOME","SOBRENOME","APELIDO","DATA","ATIVO"]
    
    for u in usuarios:
        # print(u)
        tabela.add_row(u)
    
    print(tabela)
    print(f'Registros: {len(usuarios)}')
    print()
    while True:
        opcao = input('V para voltar... ').lower()
        if opcao in ['v']:
            break
def apagarUsuario():
    pass

def salvarUsuario(usuario):
    arquivo = 'Controle_Estoque/usuario.csv'
    with open(arquivo,'a',newline='') as arq:
        arq_csv = csv.writer(arq,delimiter=",")
        arq_csv.writerow(usuario)
        
def lerUsuario():
    arquivo = 'Controle_Estoque/usuario.csv'
    with open(arquivo,'r', newline='') as arq:
        usuarios = csv.reader(arq, delimiter=",")
        usuarios = list(usuarios)
        print(f'Registros: {len(usuarios)}')
    return usuarios