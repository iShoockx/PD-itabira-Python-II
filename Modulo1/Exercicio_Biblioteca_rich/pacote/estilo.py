from rich import print
from rich.panel import Panel

""" Essa modulo utiliza da acesso a funçoes de estilizaçao da biblioteca rich"""
def muda_cor_texto(texto1,cor="red",isarquivo=False):
    """"Essa funçao recebe um texto e uma cor e imprime o texto com a cor escolhida
    
    Parametros
    ----------
    texto1 : str
        Texto que deseja estilizar ou caminho para arquivo
    isarquivo : bool,opcional
        Se True, o texto1 é um caminho para arquivo, se False, é um texto
    cor : str,opcional
        Cor que deseja estilizar o texto ex:(red,blue,green), (255,0,0) ou #FF0000

    Returns
    -------
    Mensagem com cor no Terminal    
    """
    
    if isarquivo:
        with open(texto1) as f:
            texto1 = f.read()
        print(Panel(texto1, style=cor))
    else:
        print(Panel(texto1, style=cor))

def texto_com_estilo(texto1,estilo="default",isarquivo=False):
    """Essa funçao recebe um texto e um estilo de texto e imprime o texto com a estilo de texto escolhida
    
    Parametros
    ----------
    texto1 : str
        Texto que deseja estilizar ou caminho para arquivo
    isarquivo : bool,opcional
        Se True, o texto1 é um caminho para arquivo, se False, é um texto
    estilo : str,opcional
        Estilo que deseja estilizar o texto ex:
    
    "bold"ou "b"para texto em negrito.

    "italic" ou  "i" para texto em itálico.

    "reverse" ou "r" para texto com cores de primeiro plano e de fundo invertidas.

    "strike"ou "s" para texto com uma linha atravessada.

    "underline" ou "u" para texto sublinhado
    
    Returns
    -------
    Mensagem estilizada no Terminal
    """
    
    if isarquivo:
        with open(texto1) as f:
            texto1 = f.read()
        print(Panel(texto1, style=estilo))
    else:
        print(Panel(texto1, style=estilo))

