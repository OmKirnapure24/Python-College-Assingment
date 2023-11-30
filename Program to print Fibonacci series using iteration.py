def fibonacci(n):

  if n < 0:
    print("Invalid number of terms")
    return
  
  a = 0
  b = 1
  
  print(a, end=" ")

  for i in range(1, n):

    print(b, end=" ")
    c = a + b
    a = b
    b = c
  print()

# Example
n = 10
print("Number of terms:", n)
print("Fibonacci series:", end=" ")
fibonacci(n)
