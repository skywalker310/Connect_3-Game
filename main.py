import util
import connect3
import game
import sys

def main():
    start = game.Game()
    start.play()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("you need to input who to play")
    elif len(sys.argv) < 3:
        print("need one more player")
    else:
        main()


