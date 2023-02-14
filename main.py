from utils import return_line_grid, return_position
from objetos import *
import sys

# -------------------- DOCUMENTAÇÃO ---------------------  
#
# # ----- Para rodar -----
# > python main.py inputFile.txt
#
# # -----  Modelo do arquivo input -----
#   
#   largura altura
#   posicao de inicio (coluna,linha) taxi
#   posicao de inicio (coluna,linha) passageiro
#   posicao de iniio (coluna,linha) destino
#
#   Mapa:
#   T,0,0
#   0,0,P 	
#   D,0,0
#
#   0 -> Caminho livre
#   X -> Parede
#   T -> Taxi
#   P -> Person
#   D -> Destino

#--------------------------------------------------------

def main():

    # ---- Arquivo passado via terminal ----
    input_file = sys.argv[1]
    
    # ---- Variaveis ----
    information = {}
    matrix_map_grid = []
    
    # ---- Abre arquivo txt para pegar informações do problema ----
    information = read_informations(input_file)
    
    # ---- Lista para guardar estados e custos dos nós abertos ----
    state_list = []
    open_satates  = set()

    # ---- Cria Estado inicial ----
    init_state = State(init_information)
    init_state.actual_state()    
    state_list.append(init_state)

    # ---- Cria estado final
    final_information = {'dimensions' : init_state , 
                        'taxi' : init_information['destination'],
                         'person' :  init_information['destination'] , 
                         'map': generateEndMap(init_information['map'])}
    
    # ---- Cria sucessores do estado raiz ----
    init_state.genarate_future_states()
        
    # Percorrendo todos os estados possíveis até encontrar o procurado
    for s in state_list:
        ...
        

    for tile in init_state.sucessors:
        print(tile)

    
if __name__ == '__main__': 
    main()
