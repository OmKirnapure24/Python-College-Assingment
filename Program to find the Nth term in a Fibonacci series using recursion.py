def fibonacci(n):

  if n < 0:
    print("Invalid term")
    return
  if n == 0 or n == 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

# Example
n = 10
print("Term:", n)
print("Fibonacci number:", fibonacci(n))
