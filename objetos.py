# Desenhar board:
#import gym

from utils import *
import copy

class Taxi:
    def __init__(self, start_posiiton):

        self.x = start_posiiton[0]
        self.y = start_posiiton[1]

        self.pick_up = False
        self.leave_passager = False
        
    def get_status(self):
        str_status = f" Taxi on [{self.x} , {self.y}]\n With passager : {self.pick_up}\n Leave passager in destination: {self.leave_passager}"
        return str_status

    def get_passager(self):
        self.pick_up = True

    def drop_passager(self):
        
        if(self.pick_up):
            self.pick_up = False
            self.leave_passager = True
        else:
            print('[ERROR] : Primeiro pegue o passageiro!')

class Passager:
    def __init__(self, start_posiiton):

        self.x = start_posiiton[0]
        self.y = start_posiiton[1]

        self.in_Taxi  = False
        self.in_destinantion = False
    
    def get_status(self):
        str_status = f" Passager on [{self.x} , {self.y}]\n In taxi : {self.in_Taxi}\n In destinantion : {self.in_destinantion}"
        return str_status
    
    def taxi_pick_up(self):
        self.in_Taxi = True

    def taxi_leave_up(self):
        
        if(self.in_Taxi):
            self.in_Taxi = False
            self.in_destinantion = True
        else:
            print('[ERROR] : Primeiro o passageiro deve esta no taxi!')

class Board:
    def __init__(self, dimensions, list_board , taxi_position , passager_position):
        
        self.width = dimensions[0]
        self.height = dimensions[1]
        
        self.list_map = list_board
        
        self.taxi = taxi_position
        self.passager = passager_position

        # Mapa no formato string
        self.str_map = return_str_map(list_board)
        
    def ways_possibilities(self):
        '''
        De acordo com a posicão do taxi, verificar as possibilidades de caminho (possiveis sucessores do mapa)
        Retorno : [{ Taxi position , Board sucessor , direção }]
        '''
        
        next_possible_positions = []
        
        x = self.taxi[0]
        y = self.taxi[1]
        #print(f" Taxi: x = {x} , y = {y}")
        
        # Configuração do tabuleiro caso:
        # Direita
        if(x+1 < self.width):
            if(self.list_map[y][x+1] != "X"):
                
                # Nova posicao do taxi
                new_position = [x+1, y]
                
                # Atualiza lista auxiliar do mapa
                aux_list_map = copy.deepcopy(self.list_map) 
                aux_list_map[y][x+1] = 'T'
                aux_list_map[y][x] = '0'

                # Direcao tomada
                direcao = 'RIGHT'

                dic = {'new_taxi_position': new_position , 'new_list_board': aux_list_map , 'direction': direcao}
                next_possible_positions.append(dic)

        # Esquerda
        if(x-1 >= 0):
            if(self.list_map[y][x-1] != "X"):

                # Nova posicao do taxi
                new_position = [y, x-1]
                
                # Atualiza lista auxiliar do mapa
                aux_list_map = copy.deepcopy(self.list_map) 
                aux_list_map[y][x-1] = 'T'
                aux_list_map[y][x] = '0'

                # Direcao tomada
                direcao = 'LEFT'

                dic = {'new_taxi_position': new_position , 'new_list_board': aux_list_map , 'direction': direcao}
                next_possible_positions.append(dic)

        # Cima
        if(y-1 >= 0):
            if(self.list_map[y-1][x] != "X"):

                # Nova posicao do taxi
                new_position = [y-1, x]
                
                # Atualiza lista auxiliar do mapa
                aux_list_map = copy.deepcopy(self.list_map) 
                aux_list_map[y-1][x] = 'T'
                aux_list_map[y][x] = '0'

                # Direcao tomada
                direcao = 'UP'

                dic = {'new_taxi_position': new_position , 'new_list_board': aux_list_map , 'direction': direcao}
                next_possible_positions.append(dic)    

        # Baixo
        if(y+1 < self.height):

            if(self.list_map[y+1][x] != "X"):

                # Nova posicao do taxi
                new_position = [y+1, x]
                
                # Atualiza lista auxiliar do mapa
                aux_list_map = copy.deepcopy(self.list_map) 
                aux_list_map[y+1][x] = 'T'
                aux_list_map[y][x] = '0'

                # Direcao tomada
                direcao = 'DOWN'

                dic = {'new_taxi_position': new_position , 'new_list_board': aux_list_map , 'direction': direcao}
                next_possible_positions.append(dic)   

        return next_possible_positions

class State:
    '''
    Classe que representa o estado atual do ambiente, agente e tudo que compoem o problema.
    '''

    def __init__(self, init_information):

        # Elementos:
        self.board = Board(init_information['dimensions'], init_information['map'] ,init_information['taxi'], init_information['person'])
        self.taxi = Taxi(init_information['taxi'])
        self.passager = Passager(init_information['person'])
        self.destiny = init_information['destination']
    
        self.h = 0     # Heuristica 
        self.g = 0     # State root
        self.f = 0     # Custo total

        self.hash = None
        self.sucessors = []    # ([Taxi position , Board sucessor , direção]) 

        # Verifica se taxi ja pegou passageiro
        if( (self.taxi.x == self.passager.x) and (self.taxi.y == self.passager.y)):
            self.taxi.get_passager()
            self.passager.taxi_pick_up()

        # Caso o taxi já esteja no destino com o passageiro
        if((self.taxi.pick_up and self.passager.in_Taxi) and ( (self.taxi.x == self.destiny[0]) and (self.taxi.y == self.destiny[1]))):
            self.taxi.drop_passager()
            self.passager.taxi_leave_up()
    
    def actual_state(self):
       # Mostra estado atual
       print()
       print(self.board.str_map) 
       print()

    def h_n(self, x1, y1 , x2 , y2):
        # MANHATTAN distance
        self.h = abs(x2 - x1) + abs(y2 - y1)

    def g_n(self, past_value):
        # Custo do Tile atual em relação ao inicio.
        self.g = 1 + past_value

    def f_n (self):
        # Custo total do estado
        self.f = self.h + self.g

    def genarate_future_states(self):
        # Gera sucessores do estado (nós filhos)
        self.sucessors =  self.board.ways_possibilities()
        # print(self.sucessors)
   
    def hash_function(self):
       # Gera chave única do estado atual:
       return  hash(self.board.str_map + self.taxi.get_status() + self.passager.get_status() )