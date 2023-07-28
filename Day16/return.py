#we calculate the price during purchase and store it in global variable.Later during return we acess the calculated price deom the global variable.
total_price_mobile=0 
total_price_shoe=0 
def purchase_mobile(price,brand):
    global total_price_mobile 
    if(brand=="Apple"):
        discount=10 
    else:
        discount=5 
    total_price_mobile=price-price*discount/100 
    print("Total price of the mobile",brand,"price",total_price_mobile)
def purchase_shoe(price,material):
    global total_price_shoe
    if(material=="leather"):
        tax=5 
    else:
        tax=2 
    total_price_shoe=price+price*tax/100 
    print("Total price of the mobile",material,"price",total_price_shoe)
def return_mobile():
    print("Refunded price of the mobile price",total_price_mobile)
def return_shoe():
    print("Refunded price of the mobile price",total_price_shoe)
purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")
return_mobile()