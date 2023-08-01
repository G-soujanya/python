class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id 
        self.__description=description 
        self.__price_per_quantity=price_per_quantity
    def get_item_id(self):
        return self.__item_id 
    def get_description(self):
        return self.__description 
    def get_price_per_quantity(self):
        return self.__price_per_quantity
class Bill:
    counter=1000
    def __init__(self):
        self.__bill_id=None 
        self.__bill_amount=None 
    def generate_bill_amount(self,item_quantity,items):
        Bill.counter+=1 
        self.__bill_id="B"+str(Bill.counter)
        total_amount=0
        for itemid,itemquantity in item_quantity.items():
            for item in items:
                if(itemid.lower()==item._Item__item_id.lower()):
                    total_amount+=item._Item__price_per_quantity*itemquantity
        self.__bill_amount=total_amount
    def get_bill_id(self):
        return self.__bill_id 
    def get_bill_amount(self):
        return self.__bill_amount 
class Customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name 
        self.__payment_status="Unpaid" 
    def pays_bill(self,bill):
        self.__payment_status="Paid"
        print("name",self.__customer_name,"bill id",bill._Bill__bill_id,"bill amount",bill._Bill__bill_amount)
    def get_customer_name(self):
        return self.__customer_name 
    def get_payment_status(self):
        return self.__payment_status
c=Customer("soujanya")
i=Item("10","jio",100)
i1=Item("11","airtle",200)
d={"10":100,"20":200}
b=Bill()
b.generate_bill_amount(d,[i,i1])
c.pays_bill(b)
