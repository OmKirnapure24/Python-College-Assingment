# Define a function to find the largest number in a list
def find_largest_number(lst):
    # Initialize a variable to store the largest number
    largest = lst[0]
    # Loop through each element in the list
    for num in lst:
        # Check if the element is larger than the current largest number
        if num > largest:
            # Update the largest number
            largest = num
    # Return the largest number
    return largest

# Create a list of numbers
numbers = [10, 15, 20, 25, 30, 35]

# Call the function to find the largest number in the list
largest = find_largest_number(numbers)

# Display the largest number
print("The largest number in the list is:", largest)
