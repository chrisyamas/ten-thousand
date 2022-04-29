from ten_thousand.game_logic import GameLogic, Banker
import sys


class Game:

    def __init__(self, num_rounds=4):
        self.bank = Banker()
        self.num_round = 0
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


    def handle_zilch(self, roller):
     print("****************************************")
     print("**        Zilch!!! Round over         **")
     print("****************************************")
     print(f"You banked 0 points in round {self.num_round}")
     print(f"Total score is {self.bank.balance} points")
     self.num_left = 6
     self.bank.clear_shelf()
     self.play(roller)

    def dice_banked(self):
        print(f"You banked {self.bank.bank()} points in round {self.num_round}")
        print(f"Total score is {self.bank.balance} points")
        self.num_left = 6

    def cheater(self, roll):
                print("Cheater!!! Or possibly made a typo...")
                self.print_roll(roll)
                print("Enter dice to keep, or (q)uit:")
                keep_response = input("> ").lower().replace(" ", "")
                if keep_response == "q":
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    sys.exit()
                else:
                    kept_dice = [int(x) for x in keep_response if x.isdigit()]
                    kept_dice = tuple(kept_dice)
                    return kept_dice

           

    def print_roll(self, roll):
        roll_string = ' '.join(map(str, (roll)))
        print(f"*** {roll_string} ***")



    def play(self, 
    roller=GameLogic.roll_dice, 
    scorer=GameLogic.calculate_score,
    validator=GameLogic.validate_keepers):
        if self.num_round == 0 and self.bank.shelved == 0:
            self.response = self.welcome_message()
        if self.response == "y":
           
            while True:
                if not self.bank.shelved: # conditional off of shelving dice 
                    self.num_round += 1   # it won't increment if dice shelved
                    print(f"Starting round {self.num_round}") # print statement that is repeating
                print(f"Rolling {self.num_left} dice...")
                roll = roller(self.num_left)
                self.print_roll(roll)
                if not scorer(roll):
                    self.handle_zilch(roller)
                print("Enter dice to keep, or (q)uit:")
                keep_response = input("> ").lower().replace(" ", "")
                if keep_response == "q":
                    print(f"Thanks for playing. You earned {self.bank.balance} points")
                    sys.exit()
                kept_dice = [int(x) for x in keep_response]
                kept_dice = tuple(kept_dice)
                while not validator(roll, kept_dice):
                    kept_dice = self.cheater(roll)
                if keep_response.isdigit() and len(keep_response) <= 6:
                    self.score = scorer(kept_dice)# lines to go over
                    self.bank.shelf(self.score)
                    self.num_left = self.num_left - len(kept_dice)
                if len(kept_dice) <= 6 and validator(roll, kept_dice):
                    print(f"You have {self.bank.shelved} unbanked points and {self.num_left} dice remaining")
                    print("(r)oll again, (b)ank your points or (q)uit:")
                    play_response = input("> ").replace(" ", "")
                    if play_response == "q":
                        print(f"Thanks for playing. You earned {self.bank.balance} points")
                        sys.exit()
                    elif play_response == "r":
                        if not self.num_left:
                            self.num_left = 6
                        continue
                    elif play_response == "b":
                        self.dice_banked()
                else:
                    self.cheater(roll)

                # elif response == "b":
                #     amount_banked += roll_score
                #     print(f"You banked {roll_score} points in round {self.num_round}")
                #     roll_score -= roll_score
                #     print(f"Total score is {self.bank.balance} points")
                #     new_round = True
                #     continue


if __name__ == "__main__":
    game = Game()
    game.play()
