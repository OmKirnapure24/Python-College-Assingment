def find_odd_numbers(arr):
    odd_numbers = []
    for num in arr:
        if num % 2 == 1:
            odd_numbers.append(num)
    return odd_numbers

numbers = [10, 15, 20, 25, 30, 35]
odd_numbers = find_odd_numbers(numbers)
print("The odd numbers in the array are:", odd_numbers)
