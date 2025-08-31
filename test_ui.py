from player import Player
from ui import UI

def test_ui():
    player = Player("Test Commander")
    ui = UI()
    
    ui.clear_screen()
    ui.display_header(1)
    ui.display_resources(player)
    ui.display_buildings(player)
    ui.display_units(player)
    ui.display_menu()

if __name__ == "__main__":
    test_ui()