from utils import tela_limpa
from tabuleiro import Tabuleiro
from palavras import rand_palavras

def main():
    tela_limpa()
    jogo = Tabuleiro(rand_palavras())

    while not jogo.fim_jogo():
        jogo.status_jogo()
        usuario_input = input("\nDigite uma letra: ")
        jogo.advinhar_letra(usuario_input)

    jogo.status_jogo()

    if jogo.vitoria():
        print('\nParabéns! Você venceu!!!')
        print('\nFoi bom jogar com você! Volte sempre!!!\n')
    else:
        print('\nFim de Jogo! Você perdeu!!!')
        print(f'\nA palavra era {jogo.palavra}')
        print(f'\nVolte a estudar o vocabulário de Português! \nMeu irmão recem-nascido sabe mais palavras\n')

if __name__ == '__main__':
    main()