def is_multiple_of_5(number):
    if number % 5 == 0:
        return True
    else:
        return False
number = int(input("Enter a number: "))

if is_multiple_of_5(number):
    print(number, "is a multiple of 5.")
else:
    print(number, "is not a multiple of 5.")
