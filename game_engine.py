import os
import time
from player import Player
from ui import UI
from game_data import BUILDING_COSTS, UNIT_COSTS, UNIT_REQUIREMENTS

class GameEngine:
    #Unificamos os dados do jogo. O GameEngine é o cérebro
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
            #Limpa caracteres (espaços)
            self.handle_input(choice)

            if choice != 'q':
                #A ideia é que o turno vira e os recursos serão coletados, independente da escolha, exceto se o player quiser sair (quit)
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
            print("Thanks for playing!")
        else:
            print("Invalid choice commander! Press Enter to continue...")
            input()

    def build_menu(self):
        print("\n 🏗️Construct buildings:")
        print("1. House (25 wood) - +5 population")
        print("2. Barracks (50 wood, 25 stone) - trains military")
        print("3. Market (75 wood, 50 stone, 25 gold) - improves economy")
        print("4. Back to main menu")
        
        choice = input ("What to build? ").strip()

        if choice == '1':
            success, message = self.player.build_structure('house')
            print(f"\n{message}")
        elif choice == '2':
            success, message = self.player.build_structure('barracks')
            print(f"\n{message}")
        elif choice == '3':
            success, message = self.player.build_structure('market')
            print(f"\n{message}")
        elif choice == '4':
            return
        else:
            print("Invalid option commander!")

        input("Press Enter to continue...")

    def train_menu(self):
        print("\n 💪TRAIN UNITS:")
        print("1. Villager (50 food) - gather resources")
        print("2. Soldier (60 food, 20 gold) - requires barracks")
        print("3. Archer (25 food, 45 wook, 25 gold) - requires barracks")
        print("4. Back to main menu")

        choice = input("What to train? ").strip()

        if choice == '1':
            success, message = self.player.train_unit('villager')
            print(f"\n{message}")

        elif choice == '2':
            success, message = self.player.train_unit('soldier')
            print(f"\n{message}")
        
        elif choice == '3':
            success, message = self.player.train_unit('archer')
            print(f"\n{message}")

        elif choice == '4':
            return
        else:
            print("Invalid option commander!")

        input("Press Enter to continue...")
    
    def gather_resources(self):
        print("\n Your villagers gathered extra resources!")
        old_resources = self.player.resources.copy()
        self.player.collect_resources()

        print("Resource gain this turn:")
        for resource in ['food', 'wood', 'stone', 'gold']:
            gain = self.player.resources[resource] - old_resources[resource]
            print(f" {resource.title()}: + {gain}")
        
        input("Press Enter to continue...")
        
    def view_status(self):
        print("\n📊 DETAILED STATUS")
        print(f"Commander: {self.player.name}")
        print(f"Turn: {self.turn}")
        print(f"Population: {self.player.get_population()}/{self.player.get_population_limit()}")
        print("\nResource income per turn:")
        villagers = self.player.units['villager']
        print(f" Food: +{villagers * 10} per turn")
        print(f" Wood: +{villagers * 8} per turn")
        print(f" Stone: +{villagers * 5} per turn")
        print(f" Gold: +{villagers * 6} per turn")

        print("\nBuilding costs:")
        for building, cost in BUILDING_COSTS.items():
            cost_str = ", ".join([f"{amount} {resource}" for resource, amount in cost.items() if amount > 0])
            print(f" {building.title()}: {cost_str}")

        input("Press Enter to continue...")

    def end_turn(self):
        print("\nEnding turn...")
        print("\nResources gathered!")
        self.player.collect_resources()
        self.turn +=1
        time.sleep(3)