def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]

num = int(input("Enter a number to search: "))

index = linear_search(numbers, num)

if index == -1:
    print("The number is not in the list.")
else:
    print("The number is found at index:", index)
