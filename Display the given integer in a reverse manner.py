def reverse_integer(number):
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = (reversed_number * 10) + last_digit
        number = number // 10
    return reversed_number
number = int(input("Enter an integer: "))

reversed_number = reverse_integer(number)
print("The reversed integer is", reversed_number)
