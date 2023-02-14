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
    
    # ---- Guarda todos os estados já descobertos ----
    state_list = {s}
    #print(s.hash_function())

    # ---- Guardar estados ordenados pela funcao de custo ----
    open_states_order  = []

    while (not compare_states(s, inter_state)):
        
        # Gera possições futuras do tabuleiro (sucessores do nó):
        s.genarate_future_states()

        for sc in s.sucessors:

            # Cria estados sucessores:
            info =  {'dimensions' : init_information['dimensions'], 
                    'taxi' : sc['new_taxi_position'],
                    'person' :  init_information['person'],
                    'destination' : init_information['person'], 
                    'map': sc['new_list_board']}

            st = State(info)
            #st.actual_state()

            # Verfica se estado já não foi visitado antes:
            state_closed = False
            for a in state_list:
                if(compare_states(st, a)):
                    state_closed  = True

            # Calcula custo
            if(not state_closed):
                 
                st.h_n(info['taxi'], info['destination'])
                st.g_n(s.g)
                st.f_n()
                
                open_states_order.append(st)
                state_list.add(st)

        # Ordenando os objetos com key = custo
        # Proximo estado a ser visitado (o de menor custo)
        sorted(open_states_order, key=lambda b: b.f)
        s = open_states_order.pop(0)

        
        print("\n--------------- PROXIMO ----------------\n")
        print(s.f)
        s.actual_state()
        print("Todos os estados: ")
        for i in state_list:
            print(i.taxi.get_status())
            print("-----")
        print("> Estados abertos: ")
        for j in open_states_order:
            print(i.taxi.get_status())
            print("-----")
        print("-------------------------------------------")
        
    # ---------------------------------------------------------
    # ----- Encontrando melhor distancia até o destino -----
    # ---------------------------------------------------------
    # ...

if __name__ == '__main__': 
    main()
