# Trabalho Prático I - Jogo do Labirinto

## 📋 Apresentação
Uma aplicaçao que cria um labirinto utilizando uma funçao de aleatorizaçao do labirinto além disso tem o sistema de pontuação para finalizar o jogo caso o usuario nao consiga fazer o caminho com o limite de jogadas 

## 🛠️ Projeto
Conheça a estrutura do nosso projeto

```
Aventura_no_labirinto/
│
├── Aventuras_pkg/
│   ├── __init__.py
│   │  
│   ├── jogador.py
│   │
│   ├── labirinto.py
│   │  
│   ├── utils.py    
│   │
│   └── musica_fundo.mp3
├── main.py
├── README.md
└── requirements.txt
```

## 🧠 Labirinto
O labirinto Parte de um principio de algoritmo de busca em profundidade (DFS) é um algoritmo que explora uma estrutura de dados em forma de árvore ou grafo. Assim gerando um labirinto perfeito com nenhum local fechado por 4 paredes 


## 🏁 Começando
Como jogar o labirinto

1. Baixe a pasta da Aventura_no_labirinto
2. Navegue ao diretorio no terminal
3. Crie um ambiente virtual no diretorio da pasta
    ´´´
    python -m venv ambiente
    ´´´
4. Ative o ambiente
    -- Windows(cmd):
      ```
      call ambiente\Scripts\activate
      ```
   - Linux:
      ```
      source ./ambiente/bin/activate
      ```
5. Baixe as bibliotecas 
   - Windows(cmd):
      ```
      pip install -r requirements.txt
      ```
   - Linux:
      ```
      python3 -m  pip install -r requirements.txt --break-system-packages
      ```
6. Execute o arquivo main.py
    ```
    python -m main -n "Nome de usuario"
    ```
7. Qualquer duvida execute
    ```
    python -m main -n "Nome de usuario" -h
    ```
    ou
    ```
    python -m main -n "Nome de usuario" -help
    ```


## 👨‍💻 Desenvolvedor
João Vitor Moreira Silva
PDITA079    

## 🙏 Aproveite o jogo !
