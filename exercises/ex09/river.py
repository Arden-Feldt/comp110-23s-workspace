"""File to define River class."""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

__author__ = "730566605"


class River:
    """This is the river: woosh watch it rush."""
    
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """This mf old? they a boomer?"""
        new_fish: list[Fish] = []
        for f in self.fish:
            if f.age <= 3:
                new_fish.append(f)

        new_bear: list[Bear] = []
        for b in self.bears:
            if b.age <= 5:
                new_bear.append(b)

        self.fish = new_fish
        self.bears = new_bear
        return None

    def remove_fish(self, amount: int):
        """Take that scaled mf away."""
        for i in range(amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Om nom nom chomp burp."""
        for b in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                Bear.eat(b, 1)
        return None
    
    def check_hunger(self):
        """Is it lunch time i hungry."""
        new_bear: list[Bear] = []
        for b in self.bears:
            if b.hunger_score >= 0:
                new_bear.append(b)
        self.bears = new_bear
        return None
        
    def repopulate_fish(self):
        """The fish and the bears."""
        for i in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Time for the talk?"""
        for i in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Open your eyes dummy."""
        print(f"~~~ Day {self.day}: ~~~ \nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """You know, about a week ago."""
        for i in range(7):
            self.one_river_day()
            i += 1