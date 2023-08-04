#lex_auth_0127476569131581442582
#Start writing your code here
from abc import ABCMeta,abstractmethod 
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101 
    def __init__(self,consumer_name):
        self.__consumer_name=consumer_name 
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1 
    def get_consumer_number(self):
        return self.__consumer_number 
    def get_consumer_name(self):
        return self.__consumer_name 
    @abstractmethod 
    def calculate_monthly_rent(self):
        pass 
class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        super().__init__(consumer_name)
        self.__base_pack_name=base_pack_name 
        self.__subscription_period=subscription_period
    def get_base_pack_name(self):
        return self.__base_pack_name 
    def get_subscription_period(self):
        return self.__subscription_period 
    def validate_base_pack_name(self):
        if(self.__base_pack_name=="Silver" or self.__base_pack_name=="Gold" or self.__base_pack_name=="Platinum"):
            return True 
        else:
            self.__base_pack_name=="Silver"
            print("Base package name is incorrect,set to silver")
    def calculate_monthly_rent(self):
        final_rent=0
        monthly_rent=0
        if(self.__subscription_period>=1 and self.__subscription_period<=24):
            if(self.validate_base_pack_name()==True)
                if(self.__base_pack_name=="Silver"):
                    monthly_rent=350.00 
                elif(self.__base_pack_name=="Gold"):
                    monthly_rent=440.00 
                elif(self.__base_pack_name=="Platinum"):
                    monthly_rent=560.00 
                final_rent=((rent*self.__subscription_period) - monthly_rent)/self.__subscription_period
            elif(self.__subscription_period>12):
                final_rent=((monthly_rent*self.__subscription_period)-monthly_rent)/self.__subscription_period
            else:
                final_rent=(monthly_rent*self.__subscription_period)/self.__subscription_period
            return final_rent 
        else:
            return -1

    
