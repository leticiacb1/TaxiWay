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

class State:
    '''
    Classe que representa o estado atual do ambiente, agente e tudo que compoem o problema.
    '''

    def __init__(self, init_information):

        # Dimensão
        self.width = init_information['dimensions'][0]
        self.height = init_information['dimensions'][1]

        # Elementos do tabuleiro (x,y)
        self.walls = init_information['wall']
        self.taxi = init_information['taxi']
        self.person = init_information['person']
        self.destiny = init_information['destination']

        # Estados
        self.pick_up = False
        self.in_destination = False

