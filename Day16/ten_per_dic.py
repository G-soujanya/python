#below code allows you to purchase different products.All products have discount of 10% 
def purchase_product(product_type,price):
    discount=10 
    price=price-price*discount/100 
    print("Total price of",product_type,"is",price)
purchase_product("mobile",20000)