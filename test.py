import pytest

from main import *
from utils import *

class TestClass:

    def test_grid1(self):
        
        # Resultado algorítimo
        test_file = 'Data/grid1.txt'
        r = main(test_file)

        # Estado esperado no final:
        init_env = read_informations(test_file)
        goal_env = get_goal_state(init_env)

        goal_state  = State(goal_env)
        goal_state.passenger.is_on_destiny  =True
        
        # Asserts
        assert r != None
        assert r.config() == goal_state.config()
        assert r.passenger.is_on_destiny == True

    def test_grid2(self):
        
        # Resultado algorítimo
        test_file = 'Data/grid2.txt'
        r = main(test_file)

        # Estado esperado no final:
        init_env = read_informations(test_file)
        goal_env = get_goal_state(init_env)

        goal_state  = State(goal_env)
        goal_state.passenger.is_on_destiny =True

        # Asserts
        assert r != None
        assert r.config() == goal_state.config()
        assert r.passenger.is_on_destiny == True
    

    def test_grid3(self):
        # Resultado algorítimo
        test_file = 'Data/grid3.txt'
        r = main(test_file)

        # Estado esperado no final:
        init_env = read_informations(test_file)
        goal_env = get_goal_state(init_env)

        goal_state  = State(goal_env)
        goal_state.passenger.is_on_destiny =True
        
        # Asserts
        assert r != None
        assert r.config() == goal_state.config()
        assert r.passenger.is_on_destiny == True
    
    def test_grid4(self):
        # Resultado algorítimo
        test_file = 'Data/grid4.txt'
        r = main(test_file)

        # Estado esperado no final:
        init_env = read_informations(test_file)
        goal_env = get_goal_state(init_env)

        goal_state  = State(goal_env)
        goal_state.passenger.is_on_destiny =True
        
        # Asserts
        assert r != None
        assert r.config() == goal_state.config()
        assert r.passenger.is_on_destiny == True

    def test_grid5(self):
        # Resultado algorítimo
        test_file = 'Data/grid5.txt'
        r = main(test_file)

        # Estado esperado no final:
        init_env = read_informations(test_file)
        goal_env = get_goal_state(init_env)

        goal_state  = State(goal_env)
        goal_state.passenger.is_on_destiny =True
        
        # Asserts
        assert r != None
        assert r.config() == goal_state.config()
        assert r.passenger.is_on_destiny == True

    def test_grid6(self):
        # Resultado algorítimo
        test_file = 'Data/grid6.txt'
        r = main(test_file)

        # Estado esperado no final:
        init_env = read_informations(test_file)
        goal_env = get_goal_state(init_env)

        goal_state  = State(goal_env)
        goal_state.passenger.is_on_destiny =True
        
        # Asserts
        assert r != None
        assert r.config() == goal_state.config()
        assert r.passenger.is_on_destiny == True