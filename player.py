from game_data import BUILDING_COSTS, UNIT_COSTS, UNIT_REQUIREMENTS

class Player:
    #automaticamente vai setar essas units e buildings
    def __init__(self, name):
        self.name = name
        self.resources = {
            'food': 200,
            'wood': 200,
            'stone': 100,
            'gold': 100
        }
        self.buildings = { 
            'town_center': 1,
            'house': 2,
            'barracks': 0,
            'market': 0
        }
        self.units = {
            'villager': 3,
            'soldier': 0, 
            'archer': 0
        }
        self.population_limit = 10

    def can_afford(self, cost):
        for resource, amount in cost.items(): #o código vai iterar o dicionário de custos, no game_data em cada recurso, comparando com a quantidade que o player tem atualmente
            if self.resources[resource] < amount:
                return False
        return True
    
    def spend_resources(self, cost):
        for resource, amount in cost.items():
            self.resources[resource] -= amount
    
    def collect_resources(self):
        villager_count = self.units['villager']
        self.resources['food'] += villager_count * 10
        self.resources['wood'] += villager_count * 8
        self.resources['stone'] += villager_count * 5
        self.resources['gold'] += villager_count * 6
    
    def get_population(self):
        return sum(self.units.values())
    
    def get_population_limit(self):
        return self.buildings['house'] * 5 + self.buildings['town_center'] * 5
    
    def build_structure(self, building_type):
        if building_type not in BUILDING_COSTS:
            return False, "Invalid building!"
        
        cost = BUILDING_COSTS[building_type]
        if not self.can_afford(cost):
            return False, "Not enough resources"
        
        self.spend_resources(cost)
        self.buildings[building_type] += 1
        return True, f"{building_type.title()} built succesfully!"

    def train_unit(self, unit_type):
        if unit_type not in UNIT_COSTS:
            return False, "Invalid unit type milord"
    
        cost = UNIT_COSTS[unit_type]
        if not self.can_afford(cost):
            return False, "Not enough resources"
        
        if self.get_population() >= self.get_population_limit():
            return False, "Population limit reached - build more houses"

        required_building = UNIT_REQUIREMENTS[unit_type]
        if self.buildings[required_building] == 0:
            return False, f"Need {required_building} to train {unit_type}"
        
        self.spend_resources(cost)
        self.units[unit_type] += 1
        return True, f"{unit_type.title()} trained successfully!"