from player import Player

def test_player_basics():
    player = Player("Chico Bioca")

    print("=== INITIAL STATE ===")
    print(f"Name: {player.name}")
    print(f"Resources: {player.resources}")
    print(f"Buildings: {player.buildings}")
    print(f"Units: {player.units}")
    print(f"Population: {player.get_population()}/{player.get_population_limit()}")

    print("\n=== TESTING RESOURCE COLLECTION ===")
    print("Before collection:", player.resources)
    player.collect_resources()
    print("After collection:", player.resources)

    print("\n=== TESTING RESOURCE SPENDING ===")
    cost = {'food': 50, 'wood': 25}
    print(f"Can afford {cost}:", player.can_afford(cost))
    player.spend_resources(cost)
    print("After spending:", player.resources)

    print("\n=== TESTING BUILDING ===")
    from game_data import BUILDING_COSTS
    house_cost = BUILDING_COSTS['house']
    print(f"House costs: {house_cost}")
    print(f"Can afford house: {player.can_afford(house_cost)}")

    if player.can_afford(house_cost):
        player.spend_resources(house_cost)
        player.buildings['house'] = player.buildings.get('house', 0) + 1
        print("Built a house!")
        print(f"New Buildings: {player.buildings}")

def test_advanced_features():
    print("\n" + "=" * 50)
    print("ADVANCED FEATURES TEST")
    print("=" * 50)

    player = Player("Commander")

    print("=== STARTING GAME ===")
    print(f"Population: {player.get_population()}/{player.get_population_limit()}")
    print(f"Resources: {player.resources}")

    player.collect_resources()
    print(f"\nAfter resource collection: {player.resources}")

    print("\n === BUILDING WITH NEW METHOD ===")
    success, message = player.build_structure('house')
    print(f"Build house: {success} - {message}")
    print(f"Houses now: {player.buildings['house']}")

    success, message = player.build_structure('barracks')
    print(f"Build barracks: {success} - {message}")
    print(f"Barracks now: {player.buildings['barracks']}")

    print("\n=== UNIT TRAINING WITH NEW METHODS ===")

    success, message = player.train_unit('soldier')
    print(f"Train soldier: {success} = {message}")
    print(f"Soldiers now: {player.units['soldier']}")

    print(f"\nFinal population: {player.get_population()}/{player.get_population_limit()}")
    print(f"Final resources: {player.resources}")

if __name__ == "__main__":
    test_player_basics()
    test_advanced_features()