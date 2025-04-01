from os import system, name

def tela_limpa():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')