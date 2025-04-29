import argparse

parser = argparse.ArgumentParser()
#argumento posicional
parser.add_argument('filename')
#opção que espera um parametro inteiro
parser.add_argument('-r', '--row', type=int, default=0)
#opçao interruptor liga/desliga
parser.add_argument('-i', '--inverted', action='store_true')

args = parser.parse_args() 
print(args)