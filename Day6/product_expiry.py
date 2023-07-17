#program that uses datetime module within a class.Enter manufacturing date and expiry date of the product.the program must display the years,months,and days that are left for expiry
import datetime
class product:
    def __init__(self):
        self.manufacture=datetime.date(2013,1,1)
        self.expiry=datetime.date(2024,1,1)
    def time_to_expire(self):
        today=datetime.date.today()
        if(today>self.expiry):
            print("product is already expired")
        else:
            time_left=self.expiry-today
            print('Time left:',time_left)
    def show(self):
        print("Expiry ",self.expiry)
        print("Manufactured date",self.manufacture)
x=product()
x.time_to_expire()
