from rich import print
from rich.layout import Layout
from rich.panel import Panel
layout = Layout()

""" Essa modulo utiliza da acesso a funçoes do Layout da biblioteca rich"""

def separador_coluna(texto1,texto2,isarquivo=False):
    
    """Essa funçao recebe dois textos e imprime os textos em dois paineis separados no terminal apos o carregamento da barra de progresso dos dois na vertical
    
    Parametros
    ----------
    texto1 : str
        Texto que deseja exibir ou caminho para arquivo
    texto2 : str
        Texto que deseja exibir ou caminho para arquivo
    isarquivo : bool,opcional
        Se True, o texto1 é um caminho para arquivo, se False, é um texto
        
    Returns
    ----------
    Mensagem no terminal    
    """

    if isarquivo:
        with open(texto1) as f:
            texto1 = f.read()
        with open(texto2) as f:
            texto2 = f.read()
            
        layout.split_column(
            Layout(name="upper"),
            Layout(name="lower"),
        )
        layout["upper"].update(
            Layout(Panel(texto1))
        )
        layout["lower"].update(
            Layout(Panel(texto2))
        )
        print(layout)
    else:
        layout.split_column(
            Layout(name="upper"),
            Layout(name="lower"),
        )
        layout["upper"].update(
            Layout(Panel(texto1))
        )
        layout["lower"].update(
            Layout(Panel(texto2))
        )
        print(layout)

def separador_linha(texto1,texto2,isarquivo=False):
    
    """Essa funçao recebe dois textos e imprime os textos em dois paineis separados no terminal apos o carregamento da barra de progresso dos dois na horizontal
    
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
    Mensagem no terminal    
    """

    if isarquivo:
        with open(texto1) as f:
            texto1 = f.read()
        with open(texto2) as f:
            texto2 = f.read()
            
        layout.split_row(
            Layout(name="left"),
            Layout(name="right"),
        )
        layout["left"].update(
            Layout(Panel(texto1))
        )
        layout["right"].update(
            Layout(Panel(texto2))
        )
        print(layout)
    else:
        layout.split_row(
            Layout(name="left"),
            Layout(name="right"),
        )
        layout["left"].update(
            Layout(Panel(texto1))
        )
        layout["right"].update(
            Layout(Panel(texto2))
        )
        print(layout)
