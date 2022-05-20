'''
UFRPE - Licenciatura em Computacao
Laboratorio de Programacao 1
Aluno - Andre Barros
PROJETO 2VA - Controle de Estoque

    Modulo usuario - funções para CRUD no arquivo usuario.csv

    campos:
    id_usuario
    nome
    sobrenome
    apelido
    data_atualizacao
    ativo
    
'''

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
        if id_usuario == linha[0]:
            print('Usuario já existe (ID tem de ser numeros) ! Digite um novo ID...')
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
    msg=0
    edicao_usuario = []
    usuarios = lerUsuario()
    print('EDITAR USUARIO')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_usuario = str(input('Entre com o ID do usuario (S sai...): ')).lower()
    if id_usuario in ['s']:
        return
    for u in usuarios:
        if id_usuario in u[0]:
            idx = usuarios.index(u)
        else:
            msg+=1
    if msg == len(usuarios):
        print('Usuario Inexistente... entre com ID valido da lista de usuarios...')    
        print()
        while True:
            opcao = input('V para voltar... ').lower()
            if opcao in ['v']:
                break
        return
    
    edicao = PrettyTable()
    edicao.field_names=["ID","NOME","SOBRENOME","APELIDO","DATA","ATIVO"]
    edicao.add_row(usuarios[idx])
    print(edicao)
    print()
    
    nome = str(input('Entre com o NOME do usuario: ')).title()
    sobrenome = str(input('Entre com o SOBRENOME do usuario: ')).title()
    apelido = str(input('Entre com o APELIDO do usuario: ')).upper()
    data_atualizacao = datetime.datetime.now()
    data_atualizacao = data_atualizacao.strftime("%Y/%m/%d %H:%M:%S")
    ativo = str(input('S para ativo e N para desativado: ')).lower()
    
    edicao_usuario.append(id_usuario)
    edicao_usuario.append(nome)
    edicao_usuario.append(sobrenome)
    edicao_usuario.append(apelido)
    edicao_usuario.append(data_atualizacao)
    edicao_usuario.append(ativo)
    
    usuarios.remove(usuarios[idx])
    usuarios.append(edicao_usuario)
       
    salvarUsuarioArquivo(usuarios)
    
    return
        
def listarUsuario():
    print('LISTA DE USUARIOS')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print()
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
    msg=0
    edicao_usuario = []
    usuarios = lerUsuario()
    print('APAGAR USUARIO')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_usuario = str(input('Entre com o ID do usuario (S sai...): ')).lower()
    if id_usuario in ['s']:
        return
    for u in usuarios:
        if id_usuario in u[0]:
            idx = usuarios.index(u)
        else:
            msg+=1
    if msg == len(usuarios):
        print('Usuario Inexistente... entre com ID valido da lista de usuarios...')    
        print()
        while True:
            opcao = input('V para voltar... ').lower()
            if opcao in ['v']:
                break
        return
    
    edicao = PrettyTable()
    edicao.field_names=["ID","NOME","SOBRENOME","APELIDO","DATA","ATIVO"]
    edicao.add_row(usuarios[idx])
    print(edicao)
    print()
    
    id_usuario = usuarios[idx][0]
    nome = usuarios[idx][1]
    sobrenome = usuarios[idx][2]
    apelido = usuarios[idx][3]
    data_atualizacao = usuarios[idx][4]
        
    ativo = str(input('S para ativo e N para desativado: ')).lower()
    
    edicao_usuario.append(id_usuario)
    edicao_usuario.append(nome)
    edicao_usuario.append(sobrenome)
    edicao_usuario.append(apelido)
    edicao_usuario.append(data_atualizacao)
    edicao_usuario.append(ativo)
    
    usuarios.remove(usuarios[idx])
    usuarios.append(edicao_usuario)
       
    salvarUsuarioArquivo(usuarios)
    

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
    return usuarios

def salvarUsuarioArquivo(usuario):
    arquivo = 'Controle_Estoque/usuario.csv'
    with open(arquivo,'w',newline='') as arq:
        arq_csv = csv.writer(arq,delimiter=",")
        arq_csv.writerows(usuario)