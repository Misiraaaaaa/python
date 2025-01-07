class publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("NAME OF AUTHOR : ",self.__name)
class book(publisher):
    def __init__(self,pubname,title,author):
        super().__init__(pubname)
        self.pubname=pubname
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(" BOOK TITLE :",self.title)
        print(" BOOK AUTHOR : ",self.author)
class python:
    def __init__(self,pubname, title ,author, price, pages):
        super().__init__(pubname,title,author)
        self.price=price
        self.pages=pages
    def display(self):
        super().display()
        print("PRICE OF THE BOOK : ",self.price)
        print("NUMBER OF PAGES : ",self.pages)
res=python("dc books","bookname","author",298,321)
res.display()