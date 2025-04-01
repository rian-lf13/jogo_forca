import random

palavras = [
    "casa", "montanha", "telefone", "girassol", "computador", "elefante", "jardim", "violino",
    "trem", "praia", "livro", "chocolate", "janela", "bicicleta", "foguete", "sombra", "escada",
    "abacaxi", "guitarra", "sorvete", "gramado", "relógio", "borboleta", "chave", "cachorro",
    "dinossauro", "colher", "luz", "ferramenta", "mochila", "passarinho", "espelho", "arco",
    "nuvem", "aventureiro", "banana", "mágico", "fada", "floresta", "tapete", "amarelo",
    "porta", "piano", "coelho", "tesoura", "castelo", "vento", "barco", "papagaio",
    "formiga", "cavalo", "ponte", "bolacha", "máquina", "tigre", "camiseta", "rio",
    "piscina", "televisão", "galo", "botão", "pipa", "bola", "estrela", "brinquedo",
    "camaleão", "fogueira", "avião", "lapiseira", "jacaré", "xadrez", "geladeira",
    "navio", "prato", "morcego", "pérola", "sino", "girafa", "mala", "tijolo",
    "telefone", "caneta", "lápis", "tatu", "pirata", "manteiga", "cinto", "pintura",
    "ponteiro", "flauta", "sacola", "cadeira", "escorregador", "fantasma", "baleia",
    "coroa", "violão", "lampião", "anel", "tartaruga", "espada", "camaleão", "circo"
]

def rand_palavras():
    return random.choice(palavras)