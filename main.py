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
    
    # ---- Abre arquivo txt para pegar informações do problema ----
    init_information = {}
    init_information = read_informations(input_file)
    
    # ---- Lista para: guardar estados e custos dos nós abertos ----
    state_list = []
    open_states  = set()

    # ---- Cria Estado inicial ----
    s = State(init_information)
    s.actual_state()    

    # ---- Cria estado Intermediário (Taxi com passageiro) ----
    inter_information = {'dimensions' : init_information['dimensions'] , 
                        'taxi' : init_information['person'],
                         'person' :  init_information['person'] ,
                         'destination' : init_information['destination'], 
                         'map': generateMap(init_information['map'] , 'intermediate')}

    inter_state = State(inter_information)
    inter_state.actual_state()

    # Verifica status:
    #inter_state.taxi.get_status()
    #inter_state.passager.get_status()

    # ---- Cria estado final (Taxi e passageiro no destino )----
    final_information = {'dimensions' : init_information['dimensions'] , 
                        'taxi' : init_information['destination'],
                         'person' :  init_information['destination'] ,
                         'destination' : init_information['destination'], 
                         'map': generateMap(init_information['map'] , 'final')}

    final_state = State(final_information)
    #final_state.actual_state()
   
    # Verifica status:
    #final_state.taxi.get_status()
    #final_state.passager.get_status()
    
    '''
    while (s.hash_function() != final_state):
        # ---- Cria sucessores do estado raiz ----
        s.genarate_future_states()
            
        # Percorrendo todos os estados possíveis até encontrar o procurado
        for state in state_list:
            ...
            
        for tile in init_state.sucessors:
            print(tile)
    '''
    
if __name__ == '__main__': 
    main()
