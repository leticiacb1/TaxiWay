# Desenhar board:
#import gym

class Taxi:
    def __init__(self, start_posiiton):

        self.x = start_posiiton[0]
        self.y = start_posiiton[1]

        self.pick_up = False
        self.leave_passager = False
        
    def get_posiiton(self):
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
    def __init__(self, dimensions, string_board , taxi_position , passager_position):
        
        self.width = dimensions[0]
        self.height = dimensions[1]
        
        self.str_map = string_board
        
        self.taxi = taxi_position
        self.passager = passager_position
        
        # None = Root
        self.father = None
        self.sucessors = []

    def ways_possibilities(self):
        '''
        De acordo com a posicão do taxi, verificar as possibilidades de caminho (possiveis sucessores do mapa)
        '''
        
        line = 0;
        column = 0

        next_possible_positions = []

        for tile in self.str_map:
            
            if(tile == '\n'):
                line+=1
                column = 0

            else:
                if (tile == 'T'):

                    # Verificando Direita:
                    if( self.str_map[line][column+1] != 'X') and (column + 1 < self.width):
                        next_possible_positions.append([line, column+1])
                    
                    elif( self.str_map[line+1][column] != 'X') and (line + 1 < self.height):
                        # Verificando Baixo
                        next_possible_positions.append([line+1,column])
                    
                    elif (self.str_map[line][column-1] != 'X') and (column- 1 >= 0) :
                        # Verificando Esquerda
                        next_possible_positions.append([line, column - 1])

                    elif (self.str_map[line-1, column] != 'X')  and (line - 1 >= 0):
                        # Verificando Cima
                        next_possible_positions.append([line-1, column]) 

                column+=1

        return next_possible_positions



class State:
    '''
    Classe que representa o estado atual do ambiente, agente e tudo que compoem o problema.
    '''

    def __init__(self, init_information):

        # Elementos:
        self.board = Board(init_information['dimensions'], init_information['root_map'] ,init_information['taxi'], init_information['person'])
        self.taxi = Taxi(init_information['taxi'])
        self.person = Passager(init_information['person'])
        self.destiny = init_information['destination']

        self.h = 0     # Heuristica 
        self.g = 0     # State root
        self.f = 0     # Custo total


    def h_n(self, x1, y1 , x2 , y2):
        # MANHATTAN distance
        self.h = abs(x2 - x1) + abs(y2 - y1)

    def g_n(self, past_value):
        # Custo do Tile atual em relação ao inicio.
        self.g = 1 + past_value

    def f_n (self):
        # Custo total do estado
        self.f = self.h + self.g

