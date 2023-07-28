#if the mobile brand is apple then the discount is 10% else the discount is 5% and all shoes have 2% tax and no discount.
def purchase_product(product_type,price,mobile_brand=None):
    if(product_type=="mobile"):
        if(mobile_brand=="Apple"):
            discount=10
        else:
            discount=5 
    if(product_type=="shoes"):
        discount=-2
    price=price-price*discount/100 
    print("Total price of",product_type,"is",price)
purchase_product("mobile",20000,"Apple")
purchase_product('shoes',200)