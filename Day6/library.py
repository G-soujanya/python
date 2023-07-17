#A menu driven program that keeps record of books and journals available in a library
class Book:
    def __init__(self):
        self.title=""
        self.author=""
        self.price=0
    def read(self):
        self.title=input("Enter the book title")
        self.author=input("Enter the author")
        self.price=float(input("Enter the price of book"))
    def display(self):
        print("Title",self.title)
        print("Author",self.author)
        print("Price",self.price)
        print("\n")
my_books=[]
ch='y'
while(ch=='y'):
    print('''
    1.Add New Book
    2.Display Books
    '''
    )
    choice=int(input("Enter your choice"))
    if(choice==1):
        book=Book()
        book.read()
        my_books.append(book)
    elif(choice==2):
        for i in my_books:
            i.display()
    else:
        print("invalid choice")
    ch=input("Do you want to continue.....")
print("Bye!")