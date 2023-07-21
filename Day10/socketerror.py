#program that deliberately raises a user-defined SocketError with any number of arguments and derived fron class Runtime
class SocketError(RuntimeError):
    def __init__(self,*arg):
        self.args=arg 
try:
    raise SocketError("hello","esta")
except SocketError as e:
    print(e)