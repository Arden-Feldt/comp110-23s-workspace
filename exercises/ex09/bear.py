"""File to define Bear class."""


class Bear:
    """This is a bear - Rawr."""
    
    def __init__(self):
        """This is my self bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """ONEEE DAY MORE."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Eating nom nom."""
        self.hunger_score += num_fish
        return None