"""
UFRPE - Universidade Federal Rural de Pernambuco
DC - Departamento de Computação
Curso: Licenciatura Plena em Computação
Disciplina: Programação 1
Professor: Dr. João Paulo Lima
Aluno: André Luiz Coelho Barros

Projeto:
    Quiz Math
    
Descrição:
    Jogo de Perguntas e Respostas de Matemática Fundamental.
    Com três níveis de dificuldade: Fácil, Médio e Dificil.
        Nível Fácil: Operações matemáticas de Adição e Subtração
        Nível Médio: Operações matemáticas de Adição, Subtração, Multiplicação
        Nível Dificil: Operações matemáticas de Adição, Subtração, Multiplicação e Divisão
    Cada pergunta possui três respostas, e somente uma está correta.
    Cada resposta correta, adiciona 1 ponto no nível fácil, 5 pontos no nível médio 
    e 10 pontos no nível dificil.
    O jogo guarda os 10 nomes com maior pontuação, ordenada da mais alta para a mais 
    baixa.
    O jogo inicialmente pede o nome e o nivel de dificuldade, 
    depois são sorteadas 10 perguntas para aquele nível de dificuldade.
    As perguntas com as respostas são gravadas em arquivo .csv que permitem 
    ser editados por MS Excel ou qualquer outro editor de arquivos.
    Os top 10 nomes também são guardados em arquivo.
      
"""
import time
import datetime
import modulo_util as MUT

# cria dict com chaves nome, pontuação e dificuldade [F,M,D]
score={'nome':'','pontuacao':0,'dificuldade':''}
perguntas_respostas=[]
sair = False
while not sair:
    MUT.limpar_tela()
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬')
    print('Benvindo ao Jogo Quiz Math')
    print('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
    print('1 - Iniciar jogo no modo fácil')
    print('2 - Iniciar jogo no modo médio')
    print('3 - Iniciar jogo no modo difícil')
    print('4 - Mostrar TOP 10')
    print('5 - Editar Perguntas e Respostas')
    print()
    print('S- Sair do Jogo\n')

    opcao = str(input('Escolha uma opção: ')).lower()
    if opcao in ['1','2','3','4','5','s']:
        if opcao == 's':
            MUT.limpar_tela()
            print('Saindo Aplicação... Jogo Finalizado !!!')
            time.sleep(1.5)
            sair = True
        elif opcao == '1':
            MUT.limpar_tela()
            MUT.iniciar_jogo('facil')
        elif opcao == '2':
            MUT.limpar_tela()
            MUT.iniciar_jogo('medio')
        elif opcao == '3':
            MUT.limpar_tela()
            MUT.iniciar_jogo('dificil')
        elif opcao == '4':
            MUT.limpar_tela()
            MUT.mostrar_top()
        elif opcao == '5':
            MUT.limpar_tela()
            MUT.editar_perguntas_respostas()
    else:
        print('Digite uma opção válida do menu...')
        time.sleep(1.5)
        MUT.limpar_tela()


