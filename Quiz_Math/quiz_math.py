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