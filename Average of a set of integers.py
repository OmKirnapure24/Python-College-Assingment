def average(numbers):

    total = sum(numbers)

    count = len(numbers)
    
    average = total / count
    
    return average

numbers = input("Enter the numbers separated by commas: ")

numbers = [int(n) for n in numbers.split(",")]

average = average(numbers)
print("The average of the numbers is", average)
