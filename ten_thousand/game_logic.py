import random


class GameLogic:

    def calculate_score(self):
        pass

    @staticmethod
    def roll_dice(num):
        rolls_list = []
        for i in range(num):
            rolls_list.append(random.randint(1, 6))
        return tuple(rolls_list)


class Banker:

    def __init__(self, shelf, bank, clear_shelf):
        pass
