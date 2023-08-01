#lex_auth_012751870201536512237
#Start writing your code here
class Ticket:
    counter=0 
    def __init__(self,passenger_name,source,destination):
        self.__passenger_name=passenger_name.lower()
        self.__source=source.lower() 
        self.__destination=destination.lower()
        self.__ticket_id=None 
    def validate_source_destination(self):
        if self.__source=="delhi":
            if self.__destination=="mumbai" or self.__destination=="kolkata" or self.__destination=="chennai" or self.__destination=="pune":
                return True
            else:
                return False
        else:
            return False
    def generate_ticket(self):
        if self.validate_source_destination():
            Ticket.counter+=1
            if Ticket.counter<10:
                self.__ticket_id=self.__source[0]+self.__destination[0]+str(0)+str(Ticket.counter)
            else:
                self.__ticket_id=self.__source[0]+self.__destination[0]+str(Ticket.counter)
            return self.__ticket_id.upper()
        else:
            self.__ticket_id=None
    def get_ticket_id(self):
        return self.__ticket_id 
    def get_passenger_name(self):
        return self.__passenger_name 
    def get_source(self):
        if(self.__source.lower()=="delhi"):
         return self.__source 
        else:
         print("source is not valid")
    def get_destination(self):
        if(self.__destination=="mumbai" or self.__destination=="chennai" or self.__destination=="pune" or self.__destination=="kolkata"):
         return self.__destination 
        else:
         print("destination is not valid")
t=Ticket("nithya","delhi","mumbai")
t.generate_ticket()
print(t.get_ticket_id())
print(t.get_passenger_name())
print(t.get_destination())

