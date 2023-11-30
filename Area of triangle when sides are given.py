import math
def area_of_triangle(a, b, c):
    
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

area = area_of_triangle(a, b, c)
print("The area of the triangle is", area, "square units.")
