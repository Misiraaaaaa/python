class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        area=(self.length* self.breadth)
        return area
    
    def perimeter(self):
        perimeter=(2*(self.length+self.breadth))
        return perimeter
    
rect1=Rectangle(5,6)
rect2=Rectangle(2,3)

if rect1.area()>rect2.area():
    print("rectangle 1 has greater area")
else:
    print("rectangle 2 has greater area")