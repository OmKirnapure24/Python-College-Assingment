import math
def geometric_mean(numbers):
    product = 1
    for n in numbers:
        product = product * n
    n = len(numbers)
    geometric_mean = math.pow(product, 1/n)
    return geometric_mean

numbers = input("Enter the numbers separated by commas: ")

numbers = [float(n) for n in numbers.split(",")]

geometric_mean = geometric_mean(numbers)
print("The geometric mean of the numbers is", geometric_mean)
