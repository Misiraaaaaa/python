class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth

    def area(self):
        area=round(self.__length*self.__breadth,2)
        return area
    
    def perimeter(self):
        perimeter=round(2*(self.__length*self.__breadth,2))
        return perimeter
    
    def __lt__(self,other):
        return self.area()<other.area()
    
rec1=Rectangle(5,6)
rec2=Rectangle(9,9)

if rec1<rec2:
    print("rectangle 1 smaller than rectangle 2")
else:
    print("rectangle 1 greater than rectangle 2")
