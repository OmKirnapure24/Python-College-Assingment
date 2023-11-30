import math
def circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def area(radius):
    area = math.pi * radius * radius
    return area
radius = float(input("Enter the radius of the circle: "))

circumference = circumference(radius)
area = area(radius)
print("The circumference of the circle is", circumference, "units.")
print("The area of the circle is", area, "square units.")
