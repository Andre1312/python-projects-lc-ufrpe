import os
import time

def limpaTela():
   os.system('cls' if os.name=='nt' else 'clear')

    # if os.name=='nt':
    #     print('CLS')
    #     time.sleep(3)
    #     os.system("cls")
    # elif os.name=='posix' or os.name=='unix':
    #     print('CLEAR')
    #     time.sleep(3)
    #     os.system("clear")
    # else:
    #     print('\n' * os.get_terminal_size().lines())

print(f'OS name: {os.name}')
print(f'Terminal # lines: {os.get_terminal_size()}')
while True:
    print('Sai ou Limpa =>')
    msg=input(':> ').lower()
    if msg == 's':
        print('Saindo...')
        limpaTela()
        break

    if msg == 'l':
        print('Limpando Tela')
        limpaTela()