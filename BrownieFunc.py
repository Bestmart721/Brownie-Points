import random

def generate_id():
    return int(random.random() * 543875378262)


class Account:
    def __init__(self, password, name, email):
        self.password = password
        self.name = name
        self.email = email
        self.ID = int(random.random() * 543875378262)
        
    def get_ID(self):
        return self.ID
    def get_email(self):
        return self.email
    def set_email(self,new_email):
        self.email = new_email
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name = new_name 
    def get_password(self):
        return self.email
    def set_password(self,new_password):
        self.password = new_password
        


class User(Account):
    def __init__(self, name, password, email):
        Account.__init__(self,password, name, email)
        self.coins = 0
        self.codes = []

    def get_coins(self):
        return self.coins

    def login(self, input_email, input_password):
        if (input_email == self.get_email()):
            pass

    def add_coins(self,hours):
        self.coins += hours
        return None

    def buy_discount(self,code):
        if self.coins > code.get_cost():
            self.codes = self.codes + [code]
            self.coins = self.coins - code.get_cost()
        else:
            print("Not enough coins.")
        return

    
    def show_discounts(self):
        print("You have discount codes for the following:")
        for discounts in self.codes:
            print (discounts)
        return None
        

class Business(Account):
    def __init__(self, name, email, password):
        Account.__init__(self, password, name, email)
        self.coin_tally = 0
        self.discount = 0
        self.total_donation = 0
        self.codes = []

    def add_code(self,code):
        self.codes = self.codes + [code]

        
    def apply_discount(self,price):
        self.total_donation += price*self.discount
        return price*(1-self.discount)

    def set_discount(self,disc):
        self.discount = disc

    def get_discount(self):
        return self.discount

    def receive_coin(self):
        self.coin_tally += 1
        return self.coin_tally


class Events:
    def __init__(self, title, address, date, time):
        self.title = title
        self.address=address
        self.date = date
        self.time = time

    def set_title(self,new_title):
        self.title = new_title
        return None
    def get_title(self):
        return self.title

    def set_address(self,new_address):
        self.address = new_address
        return None
    def get_address(self):
        return self.address

    def set_date(self,new_date):
        self.date = new_date
        return None
    def get_date(self):
        return self.date

    def set_time(self,new_time):
        self.time = new_time
        return None
    def get_time(self):
        return self.time


class Discount:
    def __init__(self,item_name,business,deduction=0,coin_cost=0):
        self.item_name = item_name
        self.business = business
        self.deduction = deduction   
        self.coin_cost = coin_cost
        self.code = int(random.random() * 543875378262)
        
    def get_cost(self):
        return self.coin_cost

    def __str__(self):
        return "- A $"+str(self.deduction)+" discount for a "+str(self.item_name)+" at "+str(self.business)+"."
