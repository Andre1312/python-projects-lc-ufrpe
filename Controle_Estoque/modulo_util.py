import os

def limpaTela():
# Função limpa tela do terminal
    os.system('cls' if os.name=='nt' else 'clear')