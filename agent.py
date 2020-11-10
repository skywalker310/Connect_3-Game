import util
import connect3
import game
import random

class RandomPlayer(game.Player):
    def __init__(self):
        super().__init__()
    
    def choose_action(state):
        char = util.get_arg(1)
        random_list = []
        a = 0
        for action in state.actions(char):
            print(str(a) + ": ", end = '')
            print(action)
            random_list.append(a)
            a = a+1
        random_input = random.choice(random_list)
        return random_input    

class MinimaxPlayer(game.Player):
    def __init__(self, plaer1, player2):
        super().__init__(player1, player2)
