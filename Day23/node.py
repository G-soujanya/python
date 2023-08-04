class Node:
    def __init__(self,data):
        self.__data=data 
        self.__next=None 
    def get_data(self):
        return self.__data 
    def set_data(self,data):
        return self.__data=data 
    def get_next(self):
        return self.__next 
    def set_next(self,next_node):
        self.__next_node=next_node 
item_node=Node("Sugar")
print(item_node.get_data())
class LinkedList:
    def __init__(self):
        self.__head=None 
        self.__tail=None 
    def get_head(self):
        return self.__head 
    def get_tail(self):
        return self.__tail