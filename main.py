from objetos import *
import sys

# -------------------- DOCUMENTAÇÃO ---------------------  
#
# # ----- Para rodar programa-----
# > python main.py Data/grid{numero}.txt
#
# # ----- Para rodar testes-----
# > pytest test.py
#
# # -----  Modelo do arquivo input -----
#   
#   largura altura
#   posicao de inicio (coluna,linha) taxi
#   posicao de inicio (coluna,linha) passageiro
#   posicao de iniio (coluna,linha) destino
#
#   Mapa (3x3):
#
#     1 2 3
#   X,X,X,X,X
#   X,T,0,0,X 1
#   X,0,0,P,X 2	
#   X,D,0,0,X 3
#   X,X,X,X,X   
#
#   0 -> Caminho livre
#   X -> Parede
#   T -> Taxi
#   P -> Person
#   D -> Destino
#   T+P -> Passageiro no Taxi
#   T+P+D -> (Passageiro + Taxi) no Destino

#--------------------------------------------------------

def AEstrela(root):
    # estados que ja foram vistos
    configs = [root.config()] 

    # estados inexplorados
    open_states = [root] 

    # verifica se ainda há estado para explorar
    while len(open_states) > 0:

        # Sorteia state considerando a funcao de custo
        open_states.sort(key = lambda x: x.f(), reverse = True)
        s = open_states.pop()
        
        # goal
        if s.passenger.is_on_destiny:
            return s
        
        # Gera sucessores do estado com menor custo
        for sucessor in s.genarate_future_states():
            if sucessor.config() not in configs:
                configs.append(sucessor.config())
                open_states.append(sucessor)

    return None

def main(input_file):

    # ---- Abre arquivo txt para pegar informações do problema ----
    initial_env = read_informations(input_file)
    initial_state = State(initial_env)
    if initial_env['x_taxi'] == initial_env['x_passenger'] and initial_env['y_taxi'] == initial_env['y_passenger']:
        initial_state.taxi.passenger_on_boarding = True
    
    # ----------------------
    # ----- Algoritimo -----
    # ----------------------
    
    result = AEstrela(initial_state)
    if result is not None:
        #print('Achou solucao!')
        for board in result.path:
            ...
            #print(board)
            #print('\n-----------------------------------------\n')
        
        return result
    else:
        print('Oh tristeza')
        return result

if __name__ == '__main__': 
    
    # ---- Arquivo passado via terminal ----
    input_file = sys.argv[1] 
    main(input_file)