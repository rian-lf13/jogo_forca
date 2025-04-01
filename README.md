# Forca Python Game 🚀

## Descrição
Um jogo clássico da forca implementado em Python, utilizando uma arquitetura modular para facilitar a manutenção e escalabilidade. 💻

## Estrutura do Projeto 🗂️

`main.py`</br>
`tabuleiro.py`  
`palavras.py`  
`utils.py`  
`imagens.py`

## Passo a Passo do Projeto 🔧
1. **Inicialização:**  
   O jogo é iniciado pelo `main.py`, que importa as funções e classes necessárias para rodar o jogo.
2. **Modularização:**  
   - **Separa funcionalidades:** Cada módulo (arquivo) cuida de uma parte do sistema, por exemplo:  
     - `tabuleiro.py`: Lógica do jogo e gerenciamento de tentativas.  
     - `palavras.py`: Seleção aleatória das palavras.  
     - `utils.py`: Função para limpar a tela, melhorando a experiência do usuário.  
     - `imagens.py`: Armazena as imagens ASCII do jogo.
   - **Benefícios:** Essa organização facilita a manutenção, possibilita futuras melhorias e favorece o reaproveitamento de código. 📦
3. **Execução Interativa:**  
   O usuário interage pelo terminal, inserindo letras para adivinhar a palavra secreta, com feedback visual instantâneo através das imagens e mensagens personalizadas com emojis. 😃

