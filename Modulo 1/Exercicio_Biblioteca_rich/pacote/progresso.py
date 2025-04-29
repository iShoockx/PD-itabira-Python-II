from rich import print
from rich.panel import Panel
from rich.progress import Progress
import time

""" Essa modulo utiliza da acesso a funçoes de progresso da biblioteca rich"""

def barra_de_progresso_texto(texto1,isarquivo=False):
    """Essa funçao recebe um texto e imprime o texto em um painel no terminal apos o carregamento da barra de progresso
    
    Parametros
    ----------
    texto1 : str
        Texto que deseja exibir ou caminho para arquivo
    isarquivo : bool,opcional
        Se True, o texto1 é um caminho para arquivo, se False, é um texto
        
    Returns
    -------
    Carregamento no terminal e
    Mensagem no terminal    
    """
    
    if isarquivo:
        with open(texto1) as f:
            texto1 = f.read()
        with Progress() as progress:
            task1 = progress.add_task("[red]Cooking...", total=100)

            while not progress.finished:
                progress.update(task1, advance=1) # controla o tempo de progreso
                time.sleep(0.02)
            if progress.finished: # Apos o termino da barra lança informaçao
                print(Panel(texto1))
    else:    
        with Progress() as progress:
            task1 = progress.add_task("[green]Cooking...", total=100)

            while not progress.finished:
                progress.update(task1, advance=1)
                time.sleep(0.02)
            if progress.finished:
                print(Panel(texto1))


def barra_de_progresso_dupla(texto1,texto2,isarquivo=False):
    
    """Essa funçao recebe dois textos e imprime os textos em um painel no terminal apos o carregamento da barra de progresso dos dois
    
    Parametros
    ----------
    texto1 : str
        Texto que deseja exibir ou caminho para arquivo
    texto2 : str
        Texto que deseja exibir ou caminho para arquivo
    isarquivo : bool,opcional
        Se True, o texto1 é um caminho para arquivo, se False, é um texto
        
    Returns
    -------
    Carregamento no terminal e
    Mensagem no terminal    
    """
    
    if isarquivo:
        with open(texto1) as f:
            texto1 = f.read()
        with Progress() as progress:
            task1 = progress.add_task("[cyan]Cooking...", total=100)
            task2 = progress.add_task("[magenta]Download...", total=100)

            while not progress.finished:
                progress.update(task1, advance=1)
                progress.update(task2, advance=0.8)
                time.sleep(0.02)
            if progress.finished:
                print(Panel(texto1))
                print(Panel(texto2))
    else:
        with Progress() as progress:
            task1 = progress.add_task("[cyan]Cooking...", total=100)
            task2 = progress.add_task("[magenta]Download...", total=100)

            while not progress.finished:
                progress.update(task1, advance=1)
                progress.update(task2, advance=0.8)
                time.sleep(0.02)
            if progress.finished:
                print(Panel(texto1))
                print(Panel(texto2))
