import math
def quadratic_roots(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return complex(-b/(2*a), math.sqrt(-d)/(2*a)), complex(-b/(2*a), -math.sqrt(-d)/(2*a))
    elif d == 0:
        return -b/(2*a), -b/(2*a)
    else:
        return (-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))
print("The roots of the quadratic equation are:", quadratic_roots(a, b, c))
