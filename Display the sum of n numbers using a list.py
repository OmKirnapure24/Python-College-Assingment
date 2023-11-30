def sum_list(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum
n = int(input("Enter the value of n: "))

numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

sum = sum_list(numbers)
print("The sum of the numbers is:", sum)
