import util
import connect3
import game

class HumanPlayer(game.Player):
    def __init__(self):
        super().__init__()

    def choose_action(state):
        #print(state)
        #char = util.get_arg(2)
        char = util.get_arg(1)
        a = 0
        for action in state.actions(char):
            print(str(a) + ": ", end = '')
            print(action)
            a = a+1
        user_input = input("Please choose an action: ")   
        return user_input


#driver code
#if __name__ == '__main__':
        
#    state = connect3.State('')
#    util.pprint(state)
#    test = HumanPlayer.choose_action(state)
   
