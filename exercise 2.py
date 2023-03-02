
#write a program to display "Hello" if a number entered by the user  is a multiple of five, otherwise print "Bye".

num = int(input("Enter a number: "))
if (num*5 == 0):
    print("Hello")
else: print("bye")


#create a class named circle.initialize it with length  and width.Make the methods to return the area and perimeter.
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.142*(self.radius**2)
    def perimeter(self):
        return 2*3.142*self.radius
 
r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),3))

        
#create a class named rectangle.initialize it with length  and width.Make the methods to return the area and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rect = Rectangle(length, width)
print("Area of rectangle:", rect.area())
print("Perimeter of rectangle:", rect.perimeter())

#Create a class named temperature.Make two methods:
i.convertFahrenheit - It will take celsius and will print it into Fahrenheit.
ii.covertcelsius - it will take Fahrenheit and will convert it to celsius.

>Create a class named circle and initialize it with radius.
Create two methods that will compute the area and perimeter of a circle.


class Temperature:
    def __init__(self, temp):
        self.temp = temp
    
    def convertFahrenheit(self):
        fahrenheit = (self.temp * 9/5) + 32
        print(f"{self.temp}°C is {fahrenheit}°F")
    
    def convertCelsius(self):
        celsius = (self.temp - 32) * 5/9
        print(f"{self.temp}°F is {celsius}°C")

        
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
        
