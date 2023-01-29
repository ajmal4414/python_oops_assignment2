"""
3
1.define a circle cass allowing to create a circleC(O,r) with center O(a,b) and radius r using the constructor
2define a Area()method of the class which calculates the area of the circle
3.define a perimeter() method of the class which allows you to calculate the perimeter of the circle
4.define a testbelongs()method of the class which allows to test wheateher a point A(x,y)belongs to the circle C
(O,r)or not
"""
class Circle:
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r

    def area(self):
        Area=3.14*(self.r**2)
        print("the area is", Area)

    def perimeter(self):
        perimeter=2*3.14*self.r
        print("the perimeter is",perimeter)

    def testbelong(self,x,y):
        if ((x - self.a) *(x - self.a)+(y - self.b)+ (y - self.b)<= self.r*self.r):
            return True
        else:
            return False
C=Circle(2,3,4)
x=10
y=1

if C.testbelong(x,y):
    print("inside")
else:
    print("outside")