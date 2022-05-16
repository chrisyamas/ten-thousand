# LAB - Class 06, 07, 08, and 09

## Project: Ten Thousand Game

This is a version of the classic game Dice Ten Thousand.

Our game follows the same basic score methods enumerated in the [Dice 10000 Wikipedia article](https://en.wikipedia.org/wiki/Dice_10000):

- Single fives are worth 50 points
- Single ones are worth 100 points
- Three of a kind are worth 100 points times the number rolled, except for three ones which are worth 1000 points
- If four, five, or six of a kind are rolled, each additional dice doubles the amount of dice previously rolled. For example, 4 die showing the number 3 would be 600 points and 5 die showing the number 3 would be 1200 points
  - This makes the highest possible score in a single roll 8000 for six ones (1000 for three ones, after that player multiplies the roll by two for each additional one in that series of rolling.)
- A straight from 1 to 6 is worth 1500 points. If a player fails to roll a straight they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
- Three pairs are worth 1000 points. For instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).

### Author: Christopher Yamas & Ella Svete

### How to initialize/run your application (where applicable)

- We run our tests for our application with `pytest` command in terminal while in directory. User must have a .venv and pytest installed.
- We run our game application with `python -m ten_thousand.game` command in terminal while in directory. User must have a .venv installed.
- To see the results of the bots games, run `python -m bots` command in terminal with .venv installed. To change overall outcomes of bots' games, you can adjust Pythonista's `self.unbanked_points` and `self.dice_remaining` thresholds in bots.py on lines 141 and 143, respectively, to decide how risk-averse Pythonista should be!

### Tests

- Tests may be checked by running `pytest` command in terminal with `.venv` activated.
