#This is a python file for a cafe
#menu containing items in the cafe
menu = ['Chai latte','Muffins','Eggs','Bread']
print(menu)
#create the stock value for items in the menu
stock = {'Chai latte': 6,
         'Muffins': 8,
         'Eggs': 3,
         'Bread':4
         }
#create a price dictionary containing prices for the items in stock
prices = {'Chai latte': 25,
          'Muffins': 15,
          'Eggs': 3,
          'Bread': 12
          }
#calculate the total stock worth in the Cafe
total_stock = sum(int(stock[x])*int(prices[x]) for x in prices)
print(total_stock)#print out result of the total calculation


