import random

class Account:
    def __init__(self, password, name, email):
        self.password = password
        self.name = name
        self.email = email
        self.ID = int(random.random() * 543875378262)

    def get_ID(self):
        print(self.ID)


class User(Account):
    def __init__(self, name, password, email):
        Account.__init__(self,password, name, email)
        self.coins = 0

    def get_coins(self):
        return self.coins

    def add_coins(self,hours):
        self.coins += hours
        return None

    def spend(self,cost,discount):
        if self.coins < cost:
            self.coins -= cost
        return None


class Business(Account):

    def __init__(self):
        self.coin_tally = 0
        self.discount = 0

    def set_discount(self,disc):
        self.discount = disc

    def get_discount(self):
        return self.discount

    def receive_coin(self,coins):
        self.coin_tally += coins
        return self.coin_tally

    #def apply_discount(self,cost,):