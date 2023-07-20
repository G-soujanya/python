from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class duck(animal):
    def make_sound(self):
        print("quack")
class cat(animal):
    def make_sound(self):
        print("meow")
d=duck()
d.make_sound()
c=cat()
c.make_sound()
