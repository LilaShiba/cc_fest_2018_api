my_nums = [100,34,46,100,23]

def pizza_boy(price):
    if price < 5:
        pay = price
    elif price >= 5 and price < 30:
        sub = price * 1/3
        pay = price - sub
    elif price >= 30:
        pay = price - 10
    print(pay)
    return pay

pizza_boy(30)
pizza_boy(31)
pizza_boy(5)
pizza_boy(4)




# calling our function
