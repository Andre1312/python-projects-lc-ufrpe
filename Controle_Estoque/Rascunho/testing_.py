import os
import time

def limpaTela():
   os.system('cls' if os.name=='nt' else 'clear')


print(f'OS name: {os.name}')
print(f'Terminal # lines: {os.get_terminal_size().lines}')
while True:
    print('Sai ou Limpa =>')
    msg=input(':> ').lower()
    if msg == 's':
        print('Saindo...')
        time.sleep(0.750)
        limpaTela()
        break

    if msg == 'l':
        print('Limpando Tela...')
        time.sleep(0.750)
        limpaTela()
        

while True:
        s=input('s...').lower()
        if s=='s':
            break