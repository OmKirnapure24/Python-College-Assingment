def print_numbers(n):
    if n < 0:
        return
    print(n)
    print_numbers(n-1)

n = int(input("Enter a positive integer: "))
print("The numbers from", n, "till 0 are:")
print_numbers(n)
