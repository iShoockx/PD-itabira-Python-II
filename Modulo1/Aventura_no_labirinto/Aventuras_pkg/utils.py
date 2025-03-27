from rich import print
from rich.layout import Layout
from rich.panel import Panel
import pygame
from Aventuras_pkg import jogador
from rich.console import Console
import sys
console = Console()

"""Esse modulo imprime o menu,instruções e o som"""
nome1=str
cor1=str

layout = Layout()
som = bool
def exibir_instrucoes():
    
    """ Essa funçao cria o layout e exibe instruçoes 
    
        Parametros
        ----------
        none
        
        Returns
        ----------
        Painel das informaçoes
    """
    console.clear()
    layout.split_column(
        Layout(name="cima",size=8),
        Layout(name="baixo",size=8),
    )
    
    #Setando layout
    layout["cima"].split_row(
        Layout(name="esquerda-cima",size=20),
        Layout(name="meio-cima" ,size=20),
        Layout(name="direita-cima",size=20)
    )
    
    layout["baixo"].split_row(
        Layout(name="esquerda-baixo",size=20),
        Layout(name="meio-baixo",size=20),
        Layout(name="direita-baixo",size=20),
    )
    #Colocando counteudo nos layouts
    layout["esquerda-cima"].update(
        Layout(Panel("\n      Q/ESC\n\n\n  Sair do jogo",style=cor1))
    )
    layout["meio-cima"].update(
        Layout(Panel("\n      W/↑\n\n\n Mover para cima",style=cor1))
    )
    layout["direita-cima"].update(
        Layout(Panel("A cada movimento voce gasta um ponto se chegar a zero é derrota",style=cor1))
    )
    layout["esquerda-baixo"].update(
        Layout(Panel("\n      A/←\n\n\n   Mover para\n    esquerda",style=cor1))
    )
    layout["meio-baixo"].update(
        Layout(Panel("\n      S/↓\n\n\nMover para baixo",style=cor1))
    )
    layout["direita-baixo"].update(
        Layout(Panel("\n      D/→\n\n\n   Mover para\n    direita",style=cor1))
    )

    console.print(layout)
    console.print(Panel("Caso queira retornar ao menu digite X",style=cor1,width=60))
    sair = input(" ")
    if sair == "X" or sair == "x":
        menu(nome1,cor1)


def menu(nome,cor):
    """Essa funçao abre um menu do jogo
    
        Parametros
        ----------
        nome : str
            nome de usuario que é apresentado no menu
        cor : str
            cor dos paineis 
        
        Returns
        ----------
        Um painel que voce escolhe uma opcao
        """
    console.clear()
    global nome1,cor1
    nome1=nome
    cor1=cor
    """Essa funçao exibe o menu e espera a resposta do usuario"""
    jogador.start_move(False)
    console.print(Panel(f" Bem-vindo {nome}\n\n 1-jogar \n 2-instruçoes \n 3-Sair \n", style=cor, width=50))
    opmenu = input(" ")
    match opmenu:
        case '1':
            jogador.start(nome,cor)
            jogador.start_move(True)
        case '2':
            exibir_instrucoes()
        case '3':
            sys.exit()
            
            
def derrota():
    """Essa funcao coloca a tela caso os pontos zerem"""
    jogador.start_move(False) 
    console.clear
    console.print(Panel("    Derrota",style=cor1,width=20))
    console.print(Panel("  Acabou seus \n   movimentos",style=cor1,width=20))
    
def vitoria():
    """Essa funcao coloca a tela caso os pontos zerem"""
    jogador.start_move(False) 
    console.clear
    console.print(Panel("    Vitoria",style=cor1,width=20))
    console.print(Panel("  Voce chegou \n   no final 🏆",style=cor1,width=20))
    
def musica(som):
    """Essa funçao habilita ou desabilita o som dependente do que foi passado no argparse"""    
    if not(som):
        pygame.init()
        pygame.mixer.music.load("Aventuras_pkg/musica_fundo.mp3")
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.play()

