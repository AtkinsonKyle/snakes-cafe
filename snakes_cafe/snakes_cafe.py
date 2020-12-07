print("""
************************************
**    Welcome to the Snakes Cafe  **
**    Please see our menu below.  **
**                                **
**To quit at any time, type "quit"**
************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
----------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
----------
Ice Cream
Cake
Pie

Drinks
----------
Coffee
Tea
Unicorn Tears

************************************
** What would you like to order?  **
************************************
""") 


def food_order():
  order = {
    'wings':0
  }
  print(order)
  wing_order =order['wings']
  user_input = input("please enter item you want to order: ")
  print(user_print)
  order[1] += 1