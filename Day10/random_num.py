#program that randomly generates a number.Raise a user-defined exception if the number is below 0.1
import random
class RandomError(Exception):
    pass
try:
    n=random.random()
    if(n<0.1):
        raise RandomError
    else:
        print(n)
except RandomError:
    print("value is below 0.1")