def is_even(number):
    
    if number % 2 == 0:
        
        return True
    else:
        
        return False


number = int(input("Enter a number: "))

if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
