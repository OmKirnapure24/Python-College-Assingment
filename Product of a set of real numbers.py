def product(numbers):
    product = 1
    for n in numbers:
        product = product * n
    return product
numbers = input("Enter the numbers separated by commas: ")
numbers = [float(n) for n in numbers.split(",")]

product = product(numbers)
print("The product of the numbers is", product)
