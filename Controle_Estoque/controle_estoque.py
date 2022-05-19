import os
import csv
import time
import prettytable as pt

#constantes e variaveis
TEMPO_ESPERA = 0.300
sair = False

def limpaTela():
# Função limpa tela do terminal
    os.system('cls' if os.name=='nt' else 'clear')
    
def sairAplicacao():
    return True
    
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
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        cadastroUsuario()
    if opcao=='2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        cadastroItem()
    if opcao=='3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        cadastroEstoque()
    if opcao=='4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        imprimeRelatorio()
    if opcao=='s':
        print('Selecionado S...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        return True

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
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        adicionarUsuario()
    if opcao == '2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        editarUsuario()
    if opcao == '3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        listarUsuario()
    if opcao == '4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        apagarUsuario()
    if opcao == 'v':
        print('Selecionado V...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
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
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        adicionarItem()
    if opcao == '2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()        
        editarItem()
    if opcao == '3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        listarItem()
    if opcao == '4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        apagarItem()
    if opcao == 'v':
        print('Selecionado V...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
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
    print()
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1', '2', '3', '4', 'v']:
            break
    if opcao == '1':
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        adicionarEstoque()
    if opcao == '2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        editarEstoque()
    if opcao == '3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        listarEstoque()
    if opcao == '4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        apagarEstoque()
    if opcao == 'v':
        print('Selecionado V...')
        time.sleep(TEMPO_ESPERA)
        limpaTela()
        menuPrincipal()


#
# principal
#


while not sair:
    menuPrincipal()
    if menuPrincipal() == True:
        print('Aplicação Finalizada...')
        break
