class Player:
    def __init__(self, name):
        self.name = name
        self. resources = {
            'food': 200,
            'wood': 200,
            'stone': 100,
            'gold': 100
        }
        self.buildings = { 
            'town_center': 1,
            'houses': 2,
            'barracks': 0,
            'market': 0
        }
        self.units = {
            'villagers': 3,
            'soldiers': 0, 
            'archers': 0
        }
        self.population_limit = 10

    def can_afford(self, cost):
        for resource, amount in cost.items():
            if self.resources[resource] < amount:
                return False
        return True
    
    def spend__resources(self, cost):
        for resource, amount in cost.items():
            self.resources[resource] -= amount
    
    def collect_resources(self):
        villager_count = self.units['villagers']
        self.resources['food'] += villager_count * 10
        self.resources['woord'] += villager_count * 8
        self.resources['stone'] += villager_count * 5
        self.resources['gold'] += villager_count * 6
    
    def get_population(self):
        return sum(self.units.values())
    
    def get_population_limit(self):
        return self.buildings['houses'] * 5 + self.buildings['town_center'] * 5