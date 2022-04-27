from ten_thousand.game_logic import GameLogic


class Game:

    def __init__(self):
        pass

    def play(self, roller=GameLogic.roll_dice, scorer=GameLogic.calculate_score):

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
                print(f"Starting round {num_round}")
                print("Rolling 6 dice...")
                roll_string = ' '.join(map(str, (roller(6))))

                print(f"*** {roll_string} ***")

                print("Enter dice to keep, or (q)uit:")
                response = input("> ")

                if response == "q":
                    print(f"Thanks for playing. You earned {amount_banked} points")
                    break

                else:
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
