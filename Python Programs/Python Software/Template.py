# Import Libraries
from string import Template


class Temp(Template):
        delimiter = '#'
        
def Main():

    # Initialize Cart
    cart = []
    cart.append(dict(item = 'Apple', price = 5, qty = 2))
    cart.append(dict(item = 'Fish', price = 32, qty = 4))
    cart.append(dict(item = 'Water', price = 2, qty = 2))

    root = Temp("#{item} x #{qty} = #{price}")

    total = 0
    print("Cart: ")

    for index in cart:
        print(root.substitute(index))
        total += index["price"]

    print("Total: " + str(total))

if __name__ == "__main__":
    Main()

       
        

    
    
