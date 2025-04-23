from pynput.keyboard import Listener, Key
from rich.console import Console
from rich.panel import Panel
from Aventuras_pkg import labirinto
from Aventuras_pkg import utils
import time
import sys
# Inicializa o console e as dimensões do terminal
console = Console()
width, height = console.size

inicio = bool
nome1 = str()
cor1 = str()

# Carregar labirinto

"""Modulo tem a funçao de movimentaçao do player e visualizaçao do mapa, alem de conter a funçao para dificuldade do labirinto"""
# Posição inicial do robôzinho
def setar_player_fim(x,y):
    global player_x,player_y,fim_x,fim_y,emoji_player,emoji_fim
    player_x, player_y = 0,0
    fim_x,fim_y = x-1,y-1
    emoji_player = "🥸"
    emoji_fim = "🏁"

def pode_mover(novo_x, novo_y):
    """Verifica se a nova posição não colide com uma parede
    
        Parâmetros
        ----------
        novo_x : int
            numero que define nova localizaçao no eixo x
        novo_y : int
            numero que define nova localizaçao no eixo y

        Returns
        ----------
        Dado booleano para funçao de movimentação

    """
    if pontos == 0:
        return False
    if novo_x < 0 or novo_y < 0 or novo_y >= len(ver) or novo_x >= len(ver[0]):
        return False
    # Verifica se há uma parede na nova posição
    if novo_x > player_x and ver[player_y][novo_x] != "   ":
        return False  # Tentando atravessar uma parede vertical indo para a direita
    if novo_x < player_x and ver[player_y][player_x] != "   ":
        return False  # Tentando atravessar uma parede vertical indo para a esquerda
    if novo_y > player_y and hor[novo_y][player_x] != "+  ":
        return False  # Tentando atravessar uma parede horizontal indo para baixo
    if novo_y < player_y and hor[player_y][player_x] != "+  ":
        return False  # Tentando atravessar uma parede horizontal indo para cima
    return True

# Desenha o robôzinho de acordo com as variáveis globais
def draw_player(cor):
    """Essa função desenha o labirinto e o jogador.
    
        Parametros
        ----------
        cor : String
            cor que fica as letras e o painel
        hor : list
            lista das paredes horizontais (+--)
        ver : list 
            lista das paredes verticais(|  )
        pontos : int
            contabiliza os pontos do jogador

        Returns
        ---------
        print no painel do labirinto pontos do jogador e o propio jogador
    """
    console.clear()
    console.print(Panel(f"{pontos}", width=10), style=cor)
    for y, (hor_line, ver_line) in enumerate(zip(hor, ver)):  
        console.print("".join(hor_line), style=cor)

        if y < len(ver):  
            line = "".join(ver_line)

            # Adiciona a bandeira no destino
            if y == fim_y:
                emoji_index_fim = fim_x * 3 + 1  # Ajuste para ficar no meio da célula
                if line[emoji_index_fim] == " ":
                    line = line[:emoji_index_fim] + emoji_fim  + line[emoji_index_fim + 1:]

            if y == player_y:
                emoji_index = player_x * 3 + 1
                if line[emoji_index] == " ":
                    line = line[:emoji_index] + emoji_player + line[emoji_index + 1:]

            console.print(line, style=cor)

    console.print(Panel("Caso queira sair aperte (Q) ou (ESC)", width=50, style=cor))




# altera as variáveis globais de posição do robôzinho
def move_player(key):
    """Essa funçao é ativada toda vez que uma tecla é ativada fazendo a movimentaçao do player
    """
    global player_x, player_y, inicio, pontos, limite # Adicione 'inicio' como global para poder modificá-lo
    if pontos == 0 and limite == 0:
        console.clear()
        utils.derrota()
        time.sleep(3)
        limite += 1
        utils.menu(nome1,cor1)
    else:
        

        novo_x, novo_y = player_x, player_y  # Inicializa as variáveis antes do try


        # Se pressionar 'Q', interrompe o jogo
        if key == Key.esc or (hasattr(key, 'char') and key.char.lower() == 'q'):
            inicio = False
            console.clear()
            start_move(False)
            utils.menu(nome1,cor1)
            return  # Sai da função imediatamente

        try:
            if key == Key.up or (hasattr(key, 'char') and key.char == 'w'):
                if pode_mover(player_x, player_y - 1):
                    novo_y -= 1
                    pontos -= 1
            elif key == Key.down or (hasattr(key, 'char') and key.char == 's'):
                if pode_mover(player_x, player_y + 1):
                    novo_y += 1
                    pontos -= 1
            elif key == Key.left or (hasattr(key, 'char') and key.char == 'a'):
                if pode_mover(player_x - 1, player_y):
                    novo_x -= 1
                    pontos -= 1
            elif key == Key.right or (hasattr(key, 'char') and key.char == 'd'):
                if pode_mover(player_x + 1, player_y):
                    novo_x += 1
                    pontos -= 1
                
        except AttributeError:
            pass
        if player_x == fim_x and player_y == fim_y:
            console.clear()
            utils.vitoria()  # Função para exibir mensagem de vitória
            time.sleep(3)
            utils.menu(nome1, cor1)
            return    
        player_x, player_y = novo_x, novo_y
        draw_player(cor1)

def selecionar_dificuldade(opcao):
    """Essa funçao seleciona o tamanho do mapa
    
        Parametros
        ----------
        opcao : bool
            usa o argserve para escolher a dificuldade
    """
    global width,height,pontos,op
    op = opcao
    if opcao == 1:
        width = 8
        height = 4
        pontos = 26
    elif opcao == 2:
        width = 16
        height = 8
        pontos = 75
    elif opcao == 3:
        width=32
        height=16
        pontos = 400
    else:
        print("Erro  use as opçoes(1 - Facil,2 - Medio, 3 - Dificil")
        sys.exit()

def start(nome,cor):
    'Essa funçao inciar algumas variaveis e cria o labirinto'
    global nome1,cor1,hor,ver,limite,op
    nome1=nome
    cor1=cor
    limite = 0
    selecionar_dificuldade(op)
    setar_player_fim(width,height)
    hor,ver = labirinto.criar_labirinto(width,height)
    
def start_move(start):
    """Essa funcao serve para começar e para a leitura do teclado"""
    if start:
        draw_player(cor1)
        with Listener(on_press=move_player) as listener:
            listener.join()  # O jogo continua rodando até 'Q' ser pressionado
