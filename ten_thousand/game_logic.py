import random
from collections import Counter


class GameLogic:

    def __init__(self):
        pass

    number_of = 0
    
    @staticmethod
    def validate_keepers(roll, keepers):
        verify_list = [x for x in roll]
        response_list = [x for x in keepers]


        list_length = len(response_list)
        index_count = 0
        for i in response_list:
            count_response = response_list.count(i)
            count_verify = verify_list.count(i)
            index_count += 1
            if count_response > count_verify:
                return False
            elif index_count == list_length:
                return True
            else:
                continue
        
        
        
        
        
        
        
        # verify_list = [x for x in roller_result]
        # response_list = [int(x) for x in response if x.isdigit()]


        # for i in response_list:
        #     count_response = response_list.count(i)
        #     count_verify = verify_list.count(i)
        #     if count_response > count_verify:
        #         print("Cheater!!! Or possibly made a typo...")
        #         break    
        #     else:
        #         continue
        


    @staticmethod
    def roll_dice(num):
        rolls_list = []
        for i in range(num):
            rolls_list.append(random.randint(1, 6))
        return tuple(rolls_list)

    @staticmethod
    def calculate_score(roll):
        multiple = 0
        user_score = 0
        count = Counter(roll)
        count_return = count.most_common()

        if len(count_return) == 6:
            GameLogic.number_of = 6
            return 1500

        if len(roll) == 0:
            return user_score

        if len(count_return) == 3 and len(roll) == 6:
            for x in range(3):
                if count_return[x][1] == 2:
                    multiple += 1

        if multiple == 3:
            GameLogic.number_of = 6
            return 1500

        else:
            for x in range(len(count_return)):
                dots = count_return[x][0]
                default_unit = dots * 100
                occurrence = count_return[x][1]

                if dots == 1:
                    if occurrence > 2:
                        default_unit = dots * 1000

                    else:
                        user_score += default_unit * occurrence

                if dots == 5:
                    if occurrence < 3:
                        user_score += dots * occurrence * 10

                if occurrence > 2:
                    user_score += (occurrence - 2) * default_unit

        return user_score


class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    # when you roll the dice, you want to keep these numbers
    def shelf(self, number):
        self.shelved += number
        return self.shelved

    # add points on the shelf to the total and reset

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    # remove all un-banked points

    def clear_shelf(self):
        self.shelved = 0
        return self.shelved
