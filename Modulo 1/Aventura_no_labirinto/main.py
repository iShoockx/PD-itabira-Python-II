import Aventuras_pkg
import argparse



parser = argparse.ArgumentParser()
# Nome de usuario 
parser.add_argument("-n", "--nome", type=str ,required=True
                    , help="Nome de usuario (type=str)")

#Escolher a cor
parser.add_argument("-c","--color", type=str,default="blue", help="Digite a cor que deseja ex:(blue),(#0000FF),(0,0,255) (type=str)")

#Escolha a dificuldade
parser.add_argument("-d", "--dificuldade", type=int, default=2, help="Escolha a dificuldade que deseja 1 a 3 (type=int)")

#Desabilitar Som
parser.add_argument("-s", "--som", action="store_true"
                    , help="Se ativado remove a trilha sonora do jogo")

args = parser.parse_args()


Aventuras_pkg.jogador.selecionar_dificuldade(args.dificuldade)
Aventuras_pkg.utils.musica(args.som)
Aventuras_pkg.utils.menu(args.nome,args.color)
