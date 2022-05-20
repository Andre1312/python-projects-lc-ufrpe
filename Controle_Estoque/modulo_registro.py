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
import prettytable as PT

def adicionarEstoque():
    registro = []
    registros = lerRegistro()
    print('ADICIONAR REGISTRO')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    id_registro = str(input('Entre com o ID de registro (S sai...): ')).lower()
    if id_registro in ['s']:
        return
        # testa se id_registro é unico
    for linha in registros:
        if id_registro == linha[0]:
            print('Peça já existe ! Digite um novo ID...')
            time.sleep(1)
            MUT.limpaTela()
            adicionarRegistro()
    
    id_usuario = str(input('Entre com o ID Usuario da registro: ')).title()
    id_peca = str(input('Entre com o ID Peça da registro: ')).upper()
    qtde_inicial = str(int(input('Entre com a quantidade inicial: ')))
    qtde_adicionada = str(int(input('Entre com a quantidade adicionada: ')))
    qtde_removida = str(int(input('Entre com a quantidade removida: ')))
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
    
    salvarRegistro(registro)

def editarEstoque():
    pass

def listarEstoque():
    print('LISTA ESTOQUE')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬')
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
    pass

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