#program that has a class store which keeps a record of code and price of each product.Display a menu of all products to the user and prompt him to enter the quantity of each item required.Generate a bill and display the total amount
class store:
    __item_code=[]
    __price=[]
    def get_data(self):
        for i in range(5):
            self.__item_code.append(int(input("code")))
            self.__price.append(int(input("price")))
    def display(self):
        print("ITEM\tPRICE")
        for i in range(5):
            print(self.__item_code[i],"\t",self.__price[i])
    def calculate_bill(self,quant):
        total_amount=0
        for i in range(5):
            total_amount=total_amount+quant[i]*self.__price[i]
        print("**********BILL********")
        print("ITEM\tPRICE\tQUANTITY\tSUBTOTAL")
        for i in range(5):
            print(self.__item_code[i],"\t",self.__price[i],"\t",quant[i],"\t",quant[i]*self.__price[i])
        print("total amount is",total_amount)
s=store()
s.get_data()
s.display()
q=[]
print("enter the quantity of eact item")
for i in range(5):
    q.append(int(input()))
s.calculate_bill(q)