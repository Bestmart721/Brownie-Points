from BrownieFunc import *

brandon = User("brandon","123","brandon@brandon.brandon")
ben = User("ben","123","ben")

ben.get_ID()
print(brandon.name)
print(ben.name)
brandon.get_ID()

brandon = User("brandon","coinpass","bsw@drexel.edu")
print(brandon.codes)
brandon.add_coins(10)
brandon.get_coins()

temp = Discount("Donut", "Dunkins", 1, coin_cost=.5)
coffee = Discount("Coffee", "Starbucks", 3, coin_cost=.5)
tea = Discount("Tea", "Starbucks", 2, coin_cost=.5)



brandon.buy_discount(tea)
brandon.buy_discount(coffee)
brandon.buy_discount(temp)

brandon.show_discounts()

print(brandon.login("wrong@email.edu", "password"))
print(brandon.login("bsw@drexel.edu", "password"))
print(brandon.login("bsw@drexel.edu", "coinpass"))
