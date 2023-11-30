def calculator(num1, num2, op):
  
  if op not in ["+", "-", "*", "/"]:
    print("Invalid operator")
    return
  
  if op == "+":
    result = num1 + num2
  elif op == "-":
    result = num1 - num2
  elif op == "*":
    result = num1 * num2
  elif op == "/":
    
    if num2 == 0:
      print("Cannot divide by zero")
      return
    result = num1 / num2
  
  return result

# Example
num1 = 10
num2 = 5
op = "+"
print("First number:", num1)
print("Second number:", num2)
print("Operator:", op)
print("Result:", calculator(num1, num2, op))
