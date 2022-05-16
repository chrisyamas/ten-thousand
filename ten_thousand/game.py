from ten_thousand.game_logic import GameLogic, Banker
import sys


class Game:

    def __init__(self, num_rounds=20):
        self.bank = Banker()
        self.round_num = 0
        self.num_left = 6
        self.score = 0
        self.response = ""
        self.num_rounds = num_rounds
        self.num_games = None
    
    def welcome_message(self):
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")

        self.response = input("> ").replace(" ", "")

        if self.response == "n":
            print("OK. Maybe another time")
        else:
            return self.response
    

    def handle_zilch(self):
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        print(f"You banked 0 points in round {self.round_num}")
        print(f"Total score is {self.bank.balance} points")
        self.num_left = 6
        self.round_num += 1
        self.bank.clear_shelf()
        self.num_rounds -= 1
        if self.num_rounds == 0:
            print(f"Thanks for playing. You earned {self.bank.balance} points")
            sys.exit()
        print(f"Starting round {self.round_num}")
        print(f"Rolling {self.num_left} dice...")
        self.roll = self.roller(self.num_left)
        self.cheater()


    def dice_banked(self):
        print(f"You banked {self.bank.bank()} points in round {self.round_num}")
        print(f"Total score is {self.bank.balance} points")
        self.num_left = 6
        self.num_rounds -= 1
        if self.num_rounds == 0:
            print(f"Thanks for playing. You earned {self.bank.balance} points")
            sys.exit()
            

    def cheater(self,
    scorer=GameLogic.calculate_score,
    validator=GameLogic.validate_keepers):
        kept_dice = []
        self.print_roll(self.roll)
        if not scorer(self.roll):
            self.handle_zilch()
        print("Enter dice to keep, or (q)uit:")
        keep_response = input("> ").lower().replace(" ", "")
        if keep_response == "q":
            print(f"Thanks for playing. You earned {self.bank.balance} points")
            sys.exit()
        kept_dice = [int(num) for num in keep_response]
        kept_dice = tuple(kept_dice)
        if validator(self.roll, kept_dice) is False:
            print("Cheater!!! Or possibly made a typo...")
            self.cheater()
        if keep_response.isnumeric() and len(keep_response) <= 6:
            self.score = scorer(kept_dice)
            self.bank.shelf(self.score)
            self.num_left = self.num_left - len(kept_dice)
            if len(kept_dice) <= 6 and validator(self.roll, kept_dice):
                print(f"You have {self.bank.shelved} unbanked points and {self.num_left} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                play_response = input("> ").replace(" ", "")
                if play_response == "q":
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    sys.exit()
                elif play_response == "r":
                    if not self.num_left:
                        self.num_left = 6
                    print(f"Rolling {self.num_left} dice...")
                    self.roll = self.roller(self.num_left)
                    self.cheater()
                elif play_response == "b":
                    self.dice_banked()
            else:
                print("Cheater!!! Or possibly made a typo...")
                self.cheater()


    @staticmethod
    def print_roll(roll):
        roll_input = ' '.join(map(str, roll))
        print(f"*** {roll_input} ***")


    def play(self, num_games=1,
    roller=GameLogic.roll_dice):
        self.num_games = num_games
        self.roller = roller
        if self.round_num == 0 and self.bank.shelved == 0:
            self.response = self.welcome_message()
        if self.response == "y":
            while True:
                if self.round_num >= self.num_rounds:
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    sys.exit()
                if not self.bank.shelved:
                    self.round_num += 1
                    print(f"Starting round {self.round_num}")
                    print(f"Rolling {self.num_left} dice...")
                    self.roll = self.roller(self.num_left)
                    self.cheater()


if __name__ == "__main__":
    game = Game()
    game.play()