import os
import time
from player import Player
from ui import UI

class GameEngine:
    def __init__(self):
        self.player = Player("Commander")
        self.ui = UI()
        self.turn = 1
        self.running = True

    def run(self):
        while self.running:
            self.ui.clear_screen()
            self.ui.display_header(self.turn)
            self.ui.display_resources(self.player)
            self.ui.display_buildings(self.player)
            self.ui.display_units(self.player)
            self.ui.display_menu()

            choice = input("\nEnter your choice: ").strip()
            self.handle_input(choice)

            if choice != 'q':
                self.end_turn()

    def handle_input(self, choice):
        if choice == '1':
            self.build_menu()
        elif choice == '2':
            self.train_menu()
        elif choice == '3':
            self.gather_resources()
        elif choice == '4':
            self.view_status()
        elif choice == 'q':
            self.running = False
            print("Welcome to Age of Terminal")
        else:
            print("Invalid choice commander! Press Enter to continue...")
            input()

    def build_menu(self):
        pass

    def train_menu(self):
        pass
    
    def gather_resources(self):
        pass
    
    def view_status(self):
        pass

    def end_turn(self):
        self.player.collect_resources()
        self.turn += 1
        time.sleep(1)