from utils import return_line_grid, return_position
from objetos import *
import sys

# -------------------- DOCUMENTAÇÃO ---------------------  
#
# # ----- Para rodar -----
# > python main.py Data/grid{numero}.txt
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
    #inter_state.actual_state()

    # Verifica status:
    #print(inter_state.taxi.get_status())
    #print(inter_state.passager.get_status())

    # ---- Cria estado final (Taxi e passageiro no destino )----
    final_information = {'dimensions' : init_information['dimensions'] , 
                        'taxi' : init_information['destination'],
                         'person' :  init_information['destination'] ,
                         'destination' : init_information['destination'], 
                         'map': generateMap(init_information['map'] , 'final')}

    final_state = State(final_information)
    #final_state.actual_state()
   
    # Verifica status:
    #print(final_state.taxi.get_status())
    #print(final_state.passager.get_status())
    
    # ---------------------------------------------------------
    # ----- Encontrando melhor distancia até o passageiro -----
    # ---------------------------------------------------------
    
    # ---- Guarda hash de estados já "computados" - set() ----
    state_list = {s.hash_function()}
    #print(s.hash_function())

    # ---- Guardar estados ordenados pela funcao de custo ----
    open_cost_states  = []

    while (s.hash_function() != inter_state.hash_function()):
        
        # Gera possições futuras do tabuleiro (sucessores do nó):
        s.genarate_future_states()

        for sc in s.sucessors:

            print(sc)
            # Cria estados sucessores:
            #s_sucessors = State()

            #print(x,y)
            # Caso nó não visitado:
            #if (sc.hash_function() not in state_list):

                # Adiciona estado 
                #state_list.add(sc.hash_function())

        break
 
    # ---------------------------------------------------------
    # ----- Encontrando melhor distancia até o destino -----
    # ---------------------------------------------------------
    
if __name__ == '__main__': 
    main()
