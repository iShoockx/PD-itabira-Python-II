from pacote import layout,painel,progresso,estilo
import argparse

# Dicionário para mapear os nomes dos módulos para os módulos importados
MODULOS = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

# Criando o parser de argumentos
parser = argparse.ArgumentParser(description="Chama módulos e funções dinamicamente")

# Argumentos para textos ou arquivos
parser.add_argument("-t1", "--texto1",required=True, help="Texto ou caminho para arquivo")
parser.add_argument("-t2", "--texto2",nargs="?", help="Texto ou caminho para arquivo")

# Flag para indicar se os textos são arquivos
parser.add_argument('-a', '--arquivo', action='store_true', help="Se ativado, os textos são caminhos para arquivos.")

# Escolha do módulo
parser.add_argument('-m', '--modulo', choices=MODULOS.keys(), default="layout", help="Escolha o módulo que deseja acessar.")

# Escolha da função dentro do módulo
parser.add_argument('-f', '--funcao', required=True, help="Escolha a função do módulo que deseja acessar.")

# Parse dos argumentos
args = parser.parse_args()

# Obtendo o módulo correto a partir do nome fornecido
modulo = MODULOS[args.modulo]

# Obtendo a função do módulo dinamicamente
try:
    funcao = getattr(modulo, args.funcao)
except AttributeError:
    print(f"Erro: A função '{args.funcao}' não foi encontrada no módulo '{args.modulo}'.")
    exit(1)
if args.texto2 is not None:
    resultado = funcao(args.texto1,args.texto2,args.arquivo)
else:
    resultado = funcao(args.texto1,args.arquivo)

print(resultado)
