BUILDING_COSTS = {
    'house': {'wood': 25, 'stone': 0, 'food': 0, 'gold': 0},
    'barracks': {'wood': 50, 'stone': 25, 'food': 0, 'gold': 0},
    'market': {'wood': 75, 'stone': 50, 'food': 0, 'gold': 25}
}

UNIT_COSTS = {
    'villager': {'food': 50, 'wood': 0, 'stone': 0, 'gold': 0},
    'soldier': {'food': 60, 'wood': 0, 'stone': 0, 'gold': 20},
    'archer': {'food': 25, 'wood': 45, 'stone': 0, 'gold': 25}
}

UNIT_REQUIREMENTS = {
    'villager': 'town_center',
    'soldier': 'barracks',
    'archer': 'barracks'
}