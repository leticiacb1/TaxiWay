# Desenhar board:
#import gym

from utils import *
from copy import deepcopy

class Entity:
    def __init__(self, x, y, identifier='0'):
        self.x = x
        self.y = y
        self.identifier = identifier

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __call__(self):
        return f'{self.identifier} at ({self.x}, {self.y})'

class Taxi(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'T')
        self.passenger_on_boarding = False

class Passenger(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'P')
        self.is_on_destiny = False

class Destiny(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'D')

class Board:
    def __init__(self, width, height, matrix):
        
        self.width = width
        self.height = height
        self.matrix = matrix

    def print_board(self):
        print(format_matrix(self.matrix))

class State:
    '''
    Classe que representa o estado atual do ambiente, agente e tudo que compoem o problema.
    '''

    def __init__(self, env):
        # Elementos:
        self.board = Board(env['width'], env['height'], env['matrix'])
        self.taxi = Taxi(env['x_taxi'], env['y_taxi'])
        self.passenger = Passenger(env['x_passenger'], env['y_passenger'])
        self.destiny = Destiny(env['x_destiny'], env['y_destiny'])
    
        self.g = env['g'] if 'g' in env.keys() else 0     # State root
        self.sucessors = []
        self.path = env['path'] if 'path' in env.keys() else []

    def h(self):
        if self.taxi.passenger_on_boarding:
            return abs(self.taxi.x - self.destiny.x) + abs(self.taxi.y - self.destiny.y)
        return abs(self.taxi.x - self.passenger.x) + abs(self.taxi.y - self.passenger.y)

    def f(self):
        # Custo total do estado
        return self.h() + self.g

    def config(self):
        str_map = ''.join([''.join(row) for row in self.board.matrix])
        return hash(f'{str_map}{int(self.taxi.passenger_on_boarding)}{int(self.passenger.is_on_destiny)}')

    def genarate_future_states(self):
        # Direita
        if(self.taxi.x + 1 <= self.board.width and self.board.matrix[self.taxi.y][self.taxi.x + 1] != 'X'):

            new_matrix = deepcopy(self.board.matrix)
            if self.taxi == self.destiny:
                new_matrix[self.taxi.y][self.taxi.x] = 'D'
            else:
                new_matrix[self.taxi.y][self.taxi.x] = '0'

            if self.taxi.x + 1 == self.destiny.x and self.taxi.y == self.destiny.y:
                if not self.taxi.passenger_on_boarding:
                    new_matrix[self.taxi.y][self.taxi.x + 1] = 'T+D'
                else:
                    new_matrix[self.taxi.y][self.taxi.x + 1] = 'T+P+D'
            elif self.taxi.x + 1 == self.passenger.x and self.taxi.y == self.passenger.y:
                new_matrix[self.taxi.y][self.taxi.x + 1] = 'T+P'
            else:
                if not self.taxi.passenger_on_boarding:
                    new_matrix[self.taxi.y][self.taxi.x + 1] = 'T'
                else:
                    new_matrix[self.taxi.y][self.taxi.x + 1] = 'T+P'

            env = {
                'width': self.board.width, 'height': self.board.height, 'matrix': new_matrix,
                'x_taxi': self.taxi.x + 1, 'y_taxi': self.taxi.y,
                'x_passenger': self.passenger.x + 1 if self.taxi.passenger_on_boarding else self.passenger.x, 'y_passenger': self.passenger.y,
                'x_destiny': self.destiny.x, 'y_destiny': self.destiny.y,
                'g': self.g + 1, 'path': self.path + [format_matrix(new_matrix)]
            }
            self.sucessors.append(State(env))

        # Esquerda
        if(self.taxi.x - 1 > 0 and self.board.matrix[self.taxi.y][self.taxi.x - 1] != 'X'):

            new_matrix = deepcopy(self.board.matrix)
            if self.taxi == self.destiny:
                new_matrix[self.taxi.y][self.taxi.x] = 'D'
            else:
                new_matrix[self.taxi.y][self.taxi.x] = '0'

            if self.taxi.x - 1 == self.destiny.x and self.taxi.y == self.destiny.y:
                if not self.taxi.passenger_on_boarding:
                    new_matrix[self.taxi.y][self.taxi.x - 1] = 'T+D'
                else:
                    new_matrix[self.taxi.y][self.taxi.x - 1] = 'T+P+D'
            elif self.taxi.x - 1 == self.passenger.x and self.taxi.y == self.passenger.y:
                new_matrix[self.taxi.y][self.taxi.x - 1] = 'T+P'
            else:
                if not self.taxi.passenger_on_boarding:
                    new_matrix[self.taxi.y][self.taxi.x - 1] = 'T'
                else:
                    new_matrix[self.taxi.y][self.taxi.x - 1] = 'T+P'

            env = {
                'width': self.board.width, 'height': self.board.height, 'matrix': new_matrix,
                'x_taxi': self.taxi.x - 1, 'y_taxi': self.taxi.y,
                'x_passenger': self.passenger.x - 1 if self.taxi.passenger_on_boarding else self.passenger.x, 'y_passenger': self.passenger.y,
                'x_destiny': self.destiny.x, 'y_destiny': self.destiny.y,
                'g': self.g + 1, 'path': self.path + [format_matrix(new_matrix)]
            }
            self.sucessors.append(State(env))  

        # Cima
        if(self.taxi.y - 1 > 0 and self.board.matrix[self.taxi.y - 1][self.taxi.x] != 'X'):

            new_matrix = deepcopy(self.board.matrix)
            if self.taxi == self.destiny:
                new_matrix[self.taxi.y][self.taxi.x] = 'D'
            else:
                new_matrix[self.taxi.y][self.taxi.x] = '0'

            if self.taxi.x == self.destiny.x and self.taxi.y - 1 == self.destiny.y:
                if not self.taxi.passenger_on_boarding:
                    new_matrix[self.taxi.y - 1][self.taxi.x] = 'T+D'
                else:
                    new_matrix[self.taxi.y - 1][self.taxi.x] = 'T+P+D'
            elif self.taxi.x == self.passenger.x and self.taxi.y - 1 == self.passenger.y:
                new_matrix[self.taxi.y - 1][self.taxi.x] = 'T+P'
            else:
                if not self.taxi.passenger_on_boarding:
                    new_matrix[self.taxi.y - 1][self.taxi.x] = 'T'
                else:
                    new_matrix[self.taxi.y - 1][self.taxi.x] = 'T+P'

            env = { 
                'width': self.board.width, 'height': self.board.height, 'matrix': new_matrix,
                'x_taxi': self.taxi.x , 'y_taxi': self.taxi.y - 1,
                'x_passenger': self.passenger.x, 'y_passenger': self.passenger.y - 1 if self.taxi.passenger_on_boarding else self.passenger.y,
                'x_destiny': self.destiny.x, 'y_destiny': self.destiny.y,
                'g': self.g + 1, 'path': self.path + [format_matrix(new_matrix)]
            }
            self.sucessors.append(State(env)) 

        # Baixo
        if(self.taxi.y + 1 <= self.board.height and self.board.matrix[self.taxi.y + 1][self.taxi.x] != 'X'):

            new_matrix = deepcopy(self.board.matrix)
            if self.taxi == self.destiny:
                new_matrix[self.taxi.y][self.taxi.x] = 'D'
            else:
                new_matrix[self.taxi.y][self.taxi.x] = '0'

            if self.taxi.x == self.destiny.x and self.taxi.y + 1 == self.destiny.y:
                if not self.taxi.passenger_on_boarding:
                    new_matrix[self.taxi.y + 1][self.taxi.x] = 'T+D'
                else:
                    new_matrix[self.taxi.y + 1][self.taxi.x] = 'T+P+D'
            elif self.taxi.x == self.passenger.x and self.taxi.y + 1 == self.passenger.y:
                new_matrix[self.taxi.y + 1][self.taxi.x] = 'T+P'
            else:
                if not self.taxi.passenger_on_boarding:
                    new_matrix[self.taxi.y + 1][self.taxi.x] = 'T'
                else:
                    new_matrix[self.taxi.y + 1][self.taxi.x] = 'T+P'

            env = {
                'width': self.board.width, 'height': self.board.height, 'matrix': new_matrix,
                'x_taxi': self.taxi.x , 'y_taxi': self.taxi.y + 1,
                'x_passenger': self.passenger.x, 'y_passenger': self.passenger.y + 1 if self.taxi.passenger_on_boarding else self.passenger.y,
                'x_destiny': self.destiny.x, 'y_destiny': self.destiny.y,
                'g': self.g + 1, 'path': self.path + [format_matrix(new_matrix)]
            }
            self.sucessors.append(State(env))

        # Pega passageiro
        if(self.taxi == self.passenger and not self.taxi.passenger_on_boarding):
            env = {
                'width': self.board.width, 'height': self.board.height, 'matrix': self.board.matrix,
                'x_taxi': self.taxi.x , 'y_taxi': self.taxi.y,
                'x_passenger': self.passenger.x, 'y_passenger': self.passenger.y,
                'x_destiny': self.destiny.x, 'y_destiny': self.destiny.y, 'g': self.g, 'path': self.path
            }

            s = State(env)
            s.taxi.passenger_on_boarding = True
            self.sucessors.append(s)
        
        # Deixar passageiro
        if(self.taxi == self.destiny and self.taxi.passenger_on_boarding):
            env = {
                'width': self.board.width, 'height': self.board.height, 'matrix': self.board.matrix,
                'x_taxi': self.taxi.x , 'y_taxi': self.taxi.y,
                'x_passenger': self.passenger.x, 'y_passenger': self.passenger.y,
                'x_destiny': self.destiny.x, 'y_destiny': self.destiny.y, 'g': self.g, 'path': self.path
            }

            s = State(env)
            s.taxi.passenger_on_boarding = False
            s.passenger.is_on_destiny = True
            self.sucessors.append(s)

        return self.sucessors
