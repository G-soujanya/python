#class that stores a string and all its status details such as number of uppercase characters,vowels,consonants,spaces.etc
class store:
    def __init__(self):
        self.vowels=0
        self.spaces=0
        self.consonants=0
        self.uppercase=0
        self.lowercase=0
        self.string=str(input("Enter string:"))
    def count_uppercase(self):
        for i in self.string:
            if(i.isupper()):
                self.uppercase+=1
    def count_lowercase(self):
        for i in self.string:
            if(i.islower()):
                self.lowercase+=1
    def count_spaces(self):
        for i in self.string:
            if(i==" "):
                self.spaces+=1
    def count_vowels(self):
        for i in self.string:
            if(i in ('a','e','i','o','u','A','E','I','O','U')):
                self.vowels+=1 
    def count_consonants(self):
        for i in self.string:
            if(i in ('a','e','i','o','u','A','E','I','O','U'," ")):
                pass
            else:
                self.consonants+=1
    def compute_stat(self):
        self.count_consonants()
        self.count_lowercase()
        self.count_spaces()
        self.count_uppercase()
        self.count_vowels()
    def show_status(self):
        print("%d no of vowels",self.vowels)
        print("%d no of consonants",self.consonants)
        print("%d no of spaces",self.spaces)
        print("%d no of uppercase",self.uppercase)
        print("%d no of lowercase",self.lowercase)
s=store()
s.compute_stat()
s.show_status() 
    
            