# Serão usadas as funções "suffle" (embaralhar)
# e "randrange" (sortear número aleatório em um intervalo)
from random import shuffle, randrange
import sys

"""Esse modulo cria o labirinto e retorna listas com a informaçao do labirinto"""

def criar_labirinto(w,h): #  largura e altura do labirinto
    """ Cria um labirinto aleatório e o desenha na tela em ASCII Art
        Parâmetros
        ----------    
        w : int
            w - o número de colunas do labirinto (padrão: 16)
        h : int    
            h - o número de linhas do labirinto (padrão: 8)
        
        Returns
        ---------
        hor : list
            lista de paredes horizontais do labirinto (+--)
        ver : listswsd
            lista de paredes verticais do labirinto (|  )
    """
    
    # Matriz de células visitadas (0 = não visitada, 1 = visitada)
    # Delimitada por uma linha/coluna com todos visitados (fronteira)
    # Sofre overflow nos índices negativos
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)] 
    
    # Linhas contendo as células e linhas entre-células
    # Inicia-se com todas as células disjuntas (paredes entre todas elas)
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]] # criaçao de uma parede vertical (| | | | |)
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)] # criaçao das linhas horizontais (+--+--+--+)
    
    # Define uma função para visitar uma célula ainda não visitada
    def walk(x, y):
        vis[y][x] = 1
        """
        Essa funçao visita uma célula e todas as suas células adjacentes,
        em profundidade, unindo-as ao labirinto corrente.
        """
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)] # Confere as celulas adjacentes a celular atual (x,y)
        shuffle(d) # embralha a lista de celulas adjacentes
        for (xx, yy) in d:
            if vis[yy][xx]: continue # ignora a celula se ela já foi visitada
            if xx == x: hor[max(y, yy)][x] = "+  " # se a celula adjacente estiver na mesma coluna, cria uma passagem horizontal
            if yy == y: ver[y][max(x, xx)] = "   " # se a celula adjacente estiver na mesma linha, cria uma passagem vertical 
                                                    # Em ambos os casos, o max é usado para garantir que a célula afetada (seja ela hor ou ver) corresponda à fronteira entre uma célula e a outra para evitar a criação de passagens fora do labirinto ou nos limites dele
            walk(xx, yy)
    
    walk(randrange(w), randrange(h))    # Visita a célula de origem aleatória
    return hor,ver

