from ten_thousand.game_logic import GameLogic
import sys


class Game:

    def __init__(self):
        pass
    
    def handle_six(self):
        pass

    def handle_zilch(self):
        pass

    def play(self, 
    roller=GameLogic.roll_dice, 
    scorer=GameLogic.calculate_score, 
    validator=GameLogic.validate_keepers):

        num_round = 0
        amount_banked = 0

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
        else:
            while True:
                num_round += 1
                response_valid = False
                print(f"Starting round {num_round}")
                print("Rolling 6 dice...")
                roll = roller(6)
                roll_string = ' '.join(map(str, (roll)))

                print(f"*** {roll_string} ***")

                #check for 6 or zilch
                roll_score = scorer(roll)
                if roll_score == 0:

                    print("****************************************")
                    print("**        Zilch!!! Round over         **")
                    print("****************************************")
                    print("You banked 0 points in round 1")
                    print("Total score is 0 points")
                else:
                    print("nice")
        
                
                while response_valid == False:
                    print("Enter dice to keep, or (q)uit:")
                    print(f"*** {roll_string} ***")
                    response = input("> ")

                    if response == "q":
                        print(f"Thanks for playing. You earned {amount_banked} points")
                        sys.exit()

                    else:
                        # check for cheating here
                        response_list = [int(x) for x in response if x.isdigit()]
                        keepers = tuple(response_list)
                        response_valid = validator(roll, keepers)
                        print("Cheater!!! Or possibly made a typo...")

                num_left = 6 - len(response)
                kept_dice = tuple(map(int, response))
                roll_score = scorer(kept_dice)
                print(f"You have {roll_score} unbanked points and {num_left} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")

                response = input("> ")

                if response == "q":
                    print(f"Thanks for playing. You earned {amount_banked} points")
                    break

                elif response == "b":
                    amount_banked += roll_score
                    print(f"You banked {roll_score} points in round {num_round}")
                    roll_score -= roll_score
                    print(f"Total score is {amount_banked} points")
                    continue

                elif response == "r":
                    continue


if __name__ == "__main__":
    game = Game()
    game.play()
