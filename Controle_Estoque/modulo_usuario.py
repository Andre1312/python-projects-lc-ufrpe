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
import csv
import time
import datetime
import prettytable

def adicionarUsuario():
    print('ADICIONAR USUARIO')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    
    pass

def editarUsuario():
    pass

def listarUsuario():
    usuarios=lerUsuario()
    print(usuarios)
    

def apagarUsuario():
    pass

def salvarUsuario(usuario):
    with open('usuario.csv','a') as arquivo:
        arquivo.write(usuario)
    

def lerUsuario():
    with open('usuario.csv','r') as arquivo:
        usuarios = arquivo.readlines()
    return usuarios

