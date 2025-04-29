from rich import print
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()

""" Essa modulo utiliza da acesso a funçoes do painel da biblioteca rich"""
def exibir(texto1,isarquivo=False):
    """Essa funçao recebe um texto e imprime o texto em um painel no terminal
    
    Parametros
    ----------
    texto1 : str
        Texto que deseja exibir ou caminho para arquivo
    isarquivo : bool,opcional
        Se True, o texto1 é um caminho para arquivo, se False, é um texto
        
    Returns
    -------
    Mensagem no terminal    
    """


    if isarquivo:
        with open(texto1) as f:
            texto1 = f.read()
        layout.update(
            Layout(Panel(texto1))
        )
        print(layout)
    else:
        layout.update(
            Layout(Panel(texto1))
        )
        print(layout)


def exibir_com_titulo(texto1,titulo,isarquivo=False):
    """Essa funçao recebe um texto e imprime o texto em um painel no terminal
    
    Parametros
    ----------
    texto1 : str
        Texto que deseja exibir ou caminho para arquivo
    titulo : str
        Texto que deseja exibir como titulo
    isarquivo : bool,opcional
        Se True, o texto1 é um caminho para arquivo, se False, é um texto
        
    Returns
    -------
    Mensagem no terminal com titulo   
    """

    if isarquivo:
        with open(texto1) as f:
            texto1 = f.read()
        layout.update(
            Layout(Panel(texto1,title=titulo))
        )
        print(layout)
    else:
        layout.update(
            Layout(Panel(texto1,title=titulo))
        )
        print(layout)

