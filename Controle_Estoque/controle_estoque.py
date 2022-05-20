import os
import time

import modulo_util as MUT
import modulo_usuario as MU
import modulo_peca as MP
import modulo_registro as MR

#constantes e variaveis
TEMPO_ESPERA = 0.300
sair = False

   
def sairAplicacao():
    global sair 
    sair = True
    return sair
    
def menuPrincipal():

    MUT.limpaTela()
    print('MENU PRINCIPAL')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print('1 - Cadastro de Usuario')
    print('2 - Cadastro de Peças')
    print('3 - Cadastro de Estoque')
    print('4 - Relatório de Estoque')
    print('S - SAIR')
    print()
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1','2','3','4','s']:
            break
        time.sleep(0.1)
        menuPrincipal()
    if opcao=='1':
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        cadastroUsuario()
    elif opcao=='2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        cadastroPeca()
    elif opcao=='3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        cadastroEstoque()
    elif opcao=='4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        imprimeRelatorio()
    elif opcao=='s':
        print('Selecionado S...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        sairAplicacao()

def cadastroUsuario():
    MUT.limpaTela()
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
        MUT.limpaTela()
        cadastroUsuario()
    if opcao == '1':
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MU.adicionarUsuario()
        cadastroUsuario()
    elif opcao == '2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MU.editarUsuario()
        cadastroUsuario()
    elif opcao == '3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MU.listarUsuario()
        cadastroUsuario()
    elif opcao == '4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MU.apagarUsuario()
        cadastroUsuario()
    elif opcao == 'v':
        print('Selecionado V...')
        time.sleep(TEMPO_ESPERA)
        menuPrincipal()

def cadastroPeca():
    MUT.limpaTela()
    print('CADASTRO DE PEÇAS')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print('1 - Adicionar Peça')
    print('2 - Editar Peça')
    print('3 - Listar Peças')
    print('4 - Apagar Peças')
    print('V - Voltar ao MENU PRINCIPAL')
    print()
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1', '2', '3', '4', 'v']:
            break
        MUT.limpaTela()
        cadastroPeca()
    if opcao == '1':
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MP.adicionarPeca()
    elif opcao == '2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()        
        MP.editarPeca()
    elif opcao == '3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MP.listarPeca()
    elif opcao == '4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MP.apagarPeca()
    elif opcao == 'v':
        print('Selecionado V...')
        time.sleep(TEMPO_ESPERA)
        menuPrincipal()


def cadastroEstoque():
    MUT.limpaTela()
    print('CADASTRO DE ESTOQUE')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print('1 - Adicionar Peça ao Estoque')
    print('2 - Editar Estoque')
    print('3 - Listar Estoque')
    print('4 - Apagar Estoque')
    print('V - Voltar ao MENU PRINCIPAL')
    print()
    while True:
        opcao = input(':> ').lower()
        if opcao in ['1', '2', '3', '4', 'v']:
            break
        MUT.limpaTela()
        cadastroEstoque()
    if opcao == '1':
        print('Selecionado 1...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MR.adicionarEstoque()
    elif opcao == '2':
        print('Selecionado 2...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MR.editarEstoque()
    elif opcao == '3':
        print('Selecionado 3...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MR.listarEstoque()
    elif opcao == '4':
        print('Selecionado 4...')
        time.sleep(TEMPO_ESPERA)
        MUT.limpaTela()
        MR.apagarEstoque()
    elif opcao == 'v':
        print('Selecionado V...')
        time.sleep(TEMPO_ESPERA)
        menuPrincipal()


#
# principal
#


while not sair:
    menuPrincipal()
    
    if sair == True:    
        print('Aplicação Finalizada...')
        time.sleep(TEMPO_ESPERA)
        break
