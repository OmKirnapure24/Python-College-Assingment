def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
numbers = [10, 20, 30, 40, 50]

num = int(input("Enter a number to search: "))

index = binary_search(numbers, num)
if index == -1:
    print("The number is not in the list.")
else:
    print("The number is found at index:", index)
