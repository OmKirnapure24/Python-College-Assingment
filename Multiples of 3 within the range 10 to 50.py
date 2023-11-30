def multiples_of_3(start, end):
    for i in range(start, end + 1):
        if i % 3 == 0:
            print(i, end=" ")
    print()
multiples_of_3(10, 50)
