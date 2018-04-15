import pymongo
import random

def generate_id():
    return str(int(random.random() * 543875378262))


class Brownie:
    def __init__(self):
        self.db_host = "localhost"
        self.db_port = 27017
        self.db_name = "BROWNIEDB"
        client = pymongo.MongoClient(self.db_host,self.db_port)
        self.db = client[self.db_name]

    def user_new(self, email, name, password):
        self.db.USERS.insert_one({'Email': email, 'Name': name, 'Password': password, "ID": generate_id() ,"Codes": [], "Coins":0})

    def user_login(self, input_email, input_password):
        user_info = self.db.USERS.find_one({"Email": input_email})
        print(user_info)
        if user_info:
            password = user_info['Password']
            if password == input_password:
                print("Pass + Email")
                return user_info["ID"]
            print("No Pass + Email")
            return True
        print("No Pass + No Email")
        return False

    def user_get_points(self, user_ID):
        user_info = self.db.USERS.find_one({"ID": user_ID})
        return user_info["Coins"]

    def user_buy_discount(self,user_ID,deal_ID):
        user_info = self.db.USERS.find_one({"ID": user_ID})
        deal_info = self.db.DEALS.find_one({"ID": deal_ID})
        if user_info["Coins"] >= deal_info["Coin_cost"]:
            user_info["Codes"] += [deal_ID]
            user_info["Coins"] -= deal_info["Coin_cost"]
            self.db.USERS.update_one({"ID": user_ID}, {'$set': user_info})
        else:
            return "Not enough coins."

    def user_get_discounts(self,user_ID):
        user_info = self.db.USERS.find_one({"ID": user_ID})
        deal_array = []
        for deal_ID in user_info["Codes"]:
            deal_info = self.db.DEALS.find_one({"ID": deal_ID})
            deal_array = deal_array + [deal_info]
        return deal_array

    def business_new(self, email, name, password):
        self.db.BUSINESSES.find_one({'Email': email, 'Name': name, 'Password': password, "ID": generate_id(), "Codes": [], "Coins": 0})

    def business_add_coins(self, ID, coins_add):
        bus_info = self.db.BUSINESSES.find_one({"ID": ID})
        bus_info["Coins"] += coins_add
        self.db.BUSINESSES.update_one({"ID": ID}, {'$set': bus_info})

    def business_create_discount(self,business,description,coin_cost):
        self.db.DEALS.insert_one(
            {'Business': business, "ID": generate_id(), "Description": description, "Coin_cost" : coin_cost})

    def charity_new(self, email, name, password):
        self.db.CHARITIES.find_one({'Email': email, 'Name': name, 'Password': password, "ID": generate_id(), "Max_coins": 1000, "Coins": 0})

    def charity_add_coins(self, ID, coins_add):
        char_info = self.db.CHARITIES.find_one({"ID": ID})
        char_info["Coins"] += coins_add
        self.db.CHARITIES.update_one({"ID": ID}, {'$set': char_info})

    def user_add_coins(self,char_ID, user_ID, hours):
        char_info = self.db.CHARITIES.find_one({"ID":char_ID})
        if char_info:
            user_info = self.db.USERS.find_one({"ID":user_ID})
            if user_info:
                user_info["Coins"] += hours
                self.db.USERS.update_one({"ID": user_ID}, {'$set': user_info})
            else:
                return None
        else:
            return None

    def make_event(self,title,address,date,time):
        self.db.EVENTS.insert_one({"Title":title,"Address":address,"Date":date,"Time":time,"ID":generate_id()})

    def event_get_all(self):
        event_info = []
        for EVENT in self.db.EVENTS.find():
            event_info.append(EVENT)
        return None

if __name__ == "__main__":
    test = Brownie()

    test.make_event('test','test','test','test')
    test.make_event('test2', 'test2', 'test2', 'test2')
    test.make_event('test3', 'test3', 'test3', 'test3')
    test.event_get_all()
