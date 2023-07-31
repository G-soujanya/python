class Bill:
    def __init__(self,biil_id,patient_name,bill_amount):
        self.__bill_id=bill_id 
        self.__patient_name=patient_name 
        self.__bill_amount=None
    def calculate_bill_amount(self,consultation_fees,quantity_list,price_list):
        total_bill_amount=0 
        for i in range(len(quantity_list)):
            total_bill_amount+=quantity_list[i]*price_list[i]
            self.__bill_amount=total_bill_amount 
    def get_bill_id(self):
        return self.__bill_id 
    def get_patient_name(self):
        return self.__patient_name 
    def get_bill_amount(self):
        return self.__bill_amount 
b=Bill()
b.calculate_bill_amount(100,[1,2,3],[10,20,30])
b.get_bill_id()
b.get_patient_name()
b.get_bill_amount()
    
