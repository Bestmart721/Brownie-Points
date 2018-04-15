import random
import pymongo

# MongoDB start/configure database
BROWNIEDB_HOST = 'localhost'
BROWNIEDB_PORT = 27017
BROWNIEDB_NAME = "BROWNIEDB"

client = pymongo.MongoClient(BROWNIEDB_HOST,BROWNIEDB_PORT)
db = client[BROWNIEDB_NAME]

USERS = db.USERS
EVENTS = db.EVENTS
DEALS = db.DEALS
BUSINESSES = db.BUSINESSES


def generate_id():
    return int(random.random() * 543875378262)

class Account:
    def __init__(self, password, name, email):
        self.password = password
        self.name = name
        self.email = email
        self.codes = []
        self.ID = str(int(random.random() * 543875378262))
        self.formatDB = {'Name':name,
                         'Password':password,
                         "Email": email,
                         "ID":str(self.ID),
                         "Codes":self.codes,
                         "Coins": 0
                         }
        
    def get_ID(self):
        return self.ID

    def get_email(self):
        return self.email

    def set_email(self,new_email):
        self.email = new_email

    def get_name(self):
        name = U

    def set_name(self,new_name):
        self.name = new_name

    def get_password(self):
        return self.email

    def get_codes(self):
        return self.codes

    def set_password(self,new_password):
        self.password = new_password
        

class User(Account):
    def __init__(self, name, password, email):
        Account.__init__(self,password, name, email)
        self.coins = 0
        USERS.insert_one(self.formatDB)

    def get_coins(self):
        return self.coins

    def add_coins(self,hours):
        self.coins += hours
        return None

    def readDB(self):
        result = USERS.find_one({"ID":self.ID})
        return result

    def updateDB(self):
        USERS.update_one({'ID': self.ID}, {'$set': {"Name": self.name, "Password": self.password,
                 "Email": self.email, 'Codes': self.codes, "Coins":self.coins}})

    def buy_discount(self,discount):
        if self.coins >= discount.get_cost():
            self.codes.append(discount.get_id())
            self.coins = self.coins - discount.get_cost()
            self.updateDB()
        else:
            print("Not enough coins.")
        return None


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

    def write2DB(self):
        BUSINESSES.insert_one(self.formatDB)
        return None

    def readDB(self):
        result = BUSINESSES.find_one({"ID":self.ID})
        return result

    def add_code(self,code):
        self.codes = self.codes + [code]
        return None

    def apply_discount(self,price):
        self.total_donation += price*self.discount
        return price*(1-self.discount)

    def set_discount(self,disc):
        self.discount = disc
        return None

    def get_discount(self):
        return self.discount

    def receive_coin(self):
        self.coin_tally += 1
        return self.coin_tally


class Events:
    def __init__(self, title, address, date, time):
        self.title = title
        self.address = address
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
    def __init__(self,business,description,coin_cost=0):
        self.business = business
        self.description = description
        self.coin_cost = coin_cost
        self.id = str(int(random.random() * 543875378262))
        
    def get_cost(self):
        return self.coin_cost

    def get_business(self):
        return self.business

    def get_description(self):
        return self.description

    def set_cost(self, new_cost):
        self.coin_cost = new_cost
        return None

    def set_business(self, new_business):
        self.business = new_business
        return None

    def set_description(self, new_description):
        self.description = new_description
        return None

    def get_id(self):
        return self.id

    def __str__(self):
        return "- A $"+str(self.deduction)+" discount for a "+str(self.item_name)+" at "+str(self.business)+"."


if __name__ == "__main__":
    USERS.delete_many({'Name': 'ben'})
    ben = User('ben', '123', '123@gmail.com')
    ben.updateDB()
    ben.add_coins(8)
    starbucks = Discount('starbucks', '20% off coffee', 1)
    starbucks2 = Discount('starbucks', '30% off coffee', 1)
    ben.buy_discount(starbucks)
    ben.buy_discount(starbucks2)
    ben.updateDB()
    print(ben.get_coins())
    print(ben.readDB())
    ben.login_user("123@gmail.com",'qwiuhqwe')

