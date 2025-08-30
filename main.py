import os
import time
from game_engine import GameEngine

def clear_screen():
    os.system('cls')

def main():
    print("=" * 50)
    print("AGE OF TERMINAL")
    print("=" * 50)
    print()

    game = GameEngine()
    game.run()

if __name__ == "__main__":
    main()
