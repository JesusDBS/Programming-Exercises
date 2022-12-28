import random


class Coin:
    '''
    Documentation here
    '''

    def __init__(self):
        self.heads = True
        self.tails = False

    def tossing_coin(self):
        side = random.randint(0, 1)

        if side:
            return self.heads

        return self.tails
