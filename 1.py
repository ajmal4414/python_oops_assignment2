"""
1.write a rectangle class in python language allowing you to build a rectangle with length and width attributes
1.create a perimeter() method to calculate the perimeter of the rectangle and a Area()method to calculate the area
of the rectangle
2.create a method display() that display the length,width,perimeter and area of an object created using an
inttantiation on rectangle class
3.create a parallelepipede child class inheriring from the rectangle class and width a height attribute and another volume()
method to calculate the volume of the parallelepiped
"""
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def perimeter(self):
        return 2*(self.length+self.width)

    def Area(self):
        return self.length*self.width

    def Display(self):

        print("The length of rectangle is:",self.length)
        print("The width of the rectangle is:",self.width)
        print("The perimeter  of the rectangle is:",self.perimeter())
        print("The area of rectangle is:",self.Area())

class parallelpipede(Rectangle):
    def __init__(self,length ,width,height):
        Rectangle.__init__(self,length,width)
        self.height=height

    def volume(self):
        return self.length * self.width *self.height

Rectangle1=Rectangle(7,5)
Rectangle1.Display()
Parallelpipede1=parallelpipede(7,5,2)
print("The volume of parallelpipede1 is:",Parallelpipede1.volume())