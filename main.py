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

    input_file = sys.argv[1]
    
    # Variaveis
    init_information = {}
    matrix_map_grid = []
    
    # Abre arquivo txt para pegar informações do problema:
    with open(input_file,'r') as f:
        
        num_line = 0
        
        for line in f.readlines():

            if(num_line == 0):
                x,y = return_position(line) 
                init_information['dimensions'] = [x,y]
             
            elif(num_line == 1):
                x,y = return_position(line)
                init_information['taxi'] = [x,y]
                
            elif(num_line == 2):
                x,y = return_position(line)
                init_information['person'] = [x,y]
            
            elif(num_line == 3):
                x,y = return_position(line)
                init_information['destination'] = [x,y]
            elif(num_line > 3):
                matrix_map_grid.append(return_line_grid(line))
                    
            num_line+=1
       
    init_information['root_map'] = matrix_map_grid
    
    # lista para guardar estados
    state_list = []

    # Cria Estado inicial:
    init_state = State(init_information)
    init_state.actual_state()
    
    state_list.append(init_state)
    
    # Cria sucessores do estado raiz:
    init_state.genarate_future_states()
    
    # Lista com nós abertos e seus custos:
    
    # Percorrendo todos os estados possíveis até encontrar o procurado
    for s in state_list:
        ...
        

    for tile in init_state.sucessors:
        print(tile)

    
if __name__ == '__main__': 
    main()
