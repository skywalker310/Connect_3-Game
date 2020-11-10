import util
import connect3
import sys
#import human
#import agent

class Player:
    def __init__(self):
        self.player_char = "X"


    #def choose_action(state):

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = connect3.State('')
        self.player_turn = "X"

    def play(self):
        while True:
            
            state = self.current_state
            print(state)
            turn = self.player_turn
            #print(turn)
            self.result = state.game_over()
            result = self.result
            print("Game done?: ", end = '')
            print(result)
            
            if self.result == "X":
                print("Player 1: "+str(sys.argv[1])+ " win the game")
                self.initialize_game()
                return
            elif self.result == "O":
                print("Player 2: "+str(sys.argv[2])+" win the game")
                self.initialize_game()
                return
            else:
                print("Lets start!")

                if self.player_turn == 'X':
                    #print("Start with X")
                    while self.player_turn == 'X':
                        if sys.argv[1] == 'human':
                            import human
                            run_action = human.HumanPlayer.choose_action(state)
                            print(run_action)
                            for i, action in enumerate(state.actions('X')):
                                #print("looping")
                                if str(i) == run_action:
                                    #print(action)
                                    state.execute(action)
                                    util.pprint(state)
                            self.player_turn = "O"
                            
                        if sys.argv[1] == 'random':
                            import agent
                            run_action = agent.RandomPlayer.choose_action(state)
                            print(run_action)
                            #print(type(run_action))
                            for i, action in enumerate(state.actions('X')):
                                #print("looping")
                                if i == run_action:
                                    #print(action)
                                    state.execute(action)
                                    util.pprint(state)
                            self.player_turn = "O"
                        #print("O turn")
                        #print(self.player_turn)
                    while self.player_turn == 'O':
                        if sys.argv[2] == 'human':
                            import human
                            run_action = human.HumanPlayer.choose_action(state)
                            print(run_action)
                            for i, action in enumerate(state.actions('O')):
                                #print("looping")
                                if str(i) == run_action:
                                    #print(action)
                                    state.execute(action)
                                    util.pprint(state)
                            self.player_turn = "X"
                            
                        if sys.argv[2] == 'random':
                            import agent
                            run_action = agent.RandomPlayer.choose_action(state)
                            print(run_action)
                            #print(type(run_action))
                            for i, action in enumerate(state.actions('O')):
                                #print("looping")
                                if i == run_action:
                                    #print(action)
                                    state.execute(action)
                                    util.pprint(state)
                            self.player_turn = "X"

                               
                            
            
if __name__ == '__main__':
    test = Game()
    test.play()





