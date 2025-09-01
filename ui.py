import os
class UI:
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self, turn):
        print("=" * 60)
        print(f" AGE OF TERMINAL - Turn {turn}")
        print("=" * 60)

    def display_resources(self, player):
        print("\n📜 RESOURCES:")
        print(f" 🍖 Food: {player.resources['food']}")
        print(f" 🪵 Wood: {player.resources['wood']}")
        print(f" 🪨 Stone: {player.resources['stone']}")
        print(f" 🪙 Gold: {player.resources['gold']}")

    def display_buildings(self, player):
        print("\n 🏰 BUILDINGS:")
        print(f" 🏛️ Town Center: {player.buildings['town_center']}")
        print(f" 🛖 Houses: {player.buildings['house']}")
        print(f" ⚔️ Barracks: {player.buildings['barracks']}")
        print(f" 💱 Market: {player.buildings['market']}")

    def display_units(self, player):
        population = player.get_population()
        pop_limit = player.get_population_limit()
        print(f"\n👥 UNITS ({population}/{pop_limit}):")
        print(f" 👷 Villagers: {player.units['villager']}")
        print(f" ⚔️ Soldiers: {player.units['soldier']}")
        print(f" 🏹 Archers: {player.units['archer']}")

    def display_menu(self):
        print("\n" + "=" * 40)
        print("ACTIONS:")
        print("1. Build Structures")
        print("2. Train Units")
        print("3. Gather Resources")
        print("4. View Detailed Status")
        print("Q. Quit Game")
        print("=" * 40)