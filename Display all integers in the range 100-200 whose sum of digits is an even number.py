def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
def even_sum_digits(start, end):
    for i in range(start, end + 1):
        if sum_of_digits(i) % 2 == 0:
            print(i, end=" ")
    print()

even_sum_digits(100, 200)
