from imagens import quadro

class Tabuleiro:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    def advinhar_letra(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    def fim_jogo(self):
        return self.vitoria() or (len(self.letras_erradas) == 6)

    def vitoria(self):
        return '_' not in self.esconder_palavra()

    def esconder_palavra(self):
        return ''.join(letra if letra in self.letras_escolhidas else '_' for letra in self.palavra)

    def status_jogo(self):
        print(quadro[len(self.letras_erradas)])
        print(f'\nPalavra: {self.esconder_palavra()}')
        print(f'\nLetras erradas: {", ".join(self.letras_erradas)}\n')