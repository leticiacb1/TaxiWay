# Desenhar board:
import gym

class Board:
    '''
    Classe que representa o ambiente que sofrerá ações do agente.
    '''

    def __init__(self, init_information):

        # Dimensão
        self.width = init_information['dimensions'][0]
        self.height = init_information['dimensions'][1]

        # Elementos do tabuleiro
        self.walls = init_information['wall']
        self.taxi = init_information['taxi']
        self.person = init_information['person']
        self.destiny = init_information['destination']

        # Estados
        self.pick_up = False
        self.in_destination = False

class Solver:

    def __init__(self):
        ...