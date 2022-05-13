import os
import csv
import prettytable as pt

def limpaTela():
    if os.name=='nt':
        os.system("cls")
    elif os.name=='unix' or os.name=='posix':
        os.sytem("clear")
    else:
        print('\n' * os.get_terminal_size().lines())

def menuPrincipal():

    limpaTela()
    print('MENU PRINCIPAL')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print('1 - Cadastro de Usuario')
    print('2 - Cadastro de Itens')
    print('3 - Cadastro de Estoque')
    print('4 - Relatório de Estoque')
    print('S - SAIR')
    print()
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1','2','3','4','s']:
            break
        if opcao=='1':
            cadastroUsuario()
        if opcao=='2':
            cadastroItem()
        if opcao=='3':
            cadastroEstoque()
        if opcao=='4':
            imprimeRelatorio()
        if opcao=='s':
            sairAplicacao()

def cadastroUsuario():
    limpaTela()
    print('CADASTRO DE USUARIO')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print('1 - Adicionar Novo Usuário')
    print('2 - Editar Usuário')
    print('3 - Listar Usuários')
    print('4 - Apagar Usuário')
    print('V - Voltar ao MENU PRINCIPAL')
    print()
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1', '2', '3', '4', 'v']:
            break
        if opcao == '1':
            adicionarUsuario()
        if opcao == '2':
            editarUsuario()
        if opcao == '3':
            listarUsuario()
        if opcao == '4':
            apagarUsuario()
        if opcao == 'v':
            menuPrincipal()

def cadastroItem():
    limpaTela()
    print('CADASTRO DE ITENS')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print('1 - Adicionar Novo Item')
    print('2 - Editar Item')
    print('3 - Listar Itens')
    print('4 - Apagar Itens')
    print('V - Voltar ao MENU PRINCIPAL')
    print()
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1', '2', '3', '4', 'v']:
            break
        if opcao == '1':
            adicionarItem()
        if opcao == '2':
            editarItem()
        if opcao == '3':
            listarItem()
        if opcao == '4':
            apagarItem()
        if opcao == 'v':
            menuPrincipal()


def cadastroEstoque():
    limpaTela()
    print('CADASTRO DE ESTOQUE')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print('1 - Adicionar Item ao Estoque')
    print('2 - Editar Estoque')
    print('3 - Listar Estoque')
    print('4 - Apagar Estoque')
    print('V - Voltar ao MENU PRINCIPAL')
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1', '2', '3', '4', 'v']:
            break
        if opcao == '1':
            adicionarEstoque()
        if opcao == '2':
            editarEstoque()
        if opcao == '3':
            listarEstoque()
        if opcao == '4':
            apagarEstoque()
        if opcao == 'v':
            menuPrincipal()


#
# principal
#

while True:
    menuPrincipal
