# Desenhar board:
#import gym

from utils import *

class Taxi:
    def __init__(self, start_posiiton):

        self.x = start_posiiton[0]
        self.y = start_posiiton[1]

        self.pick_up = False
        self.leave_passager = False
        
    def get_position(self):
        print(f" Taxi on [{self.x} , {self.y}]")

    def update_position(self , new_x , new_y):
        self.x = new_x
        self.y = new_y

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
        print(f"Passager start on [{self.x} , {self.y}]")
        print(f"In taxi : {self.in_Taxi}")
    
    def taxi_pick_up(self):
        self.in_Taxi = True

    def taxi_leave_up(self):
        self.in_Taxi = False

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
        '''
        
        next_possible_positions = []
        
        x = self.taxi[0]
        y = self.taxi[1]
        #print(f" Taxi: x = {x} , y = {y}")
        
        # Direita
        if(x+1 < self.width):
            if(self.list_map[y][x+1] != "X"):
                next_possible_positions.append([x+1,y])

        # Esquerda
        if(x-1 >= 0):
            if(self.list_map[y][x-1] != "X"):
                next_possible_positions.append([x-1,y])
        # Cima
        if(y-1 >= 0):
             if(self.list_map[y-1][x] != "X"):
                next_possible_positions.append([x,y-1])
        # Baixo
        if(y+1 < self.height):
            if(self.list_map[y+1][x] != "X"):
                next_possible_positions.append([x,y+1])

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
        self.father = None  # Root (Init)
        self.sucessors = []
    
    def actual_state(self):
       # Mostra estado atual
       self
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
        print(self.sucessors)
   
    def hash_function(self):
       # Gera chave única do estado atual:
       return str(hash(self.board.str_map + self.taxi.get_posiiton() + str(self.passager.in_destinantion)))


