def is_palindrome(string):
  string = string.lower()
  reversed_string = string[::-1]
  if string == reversed_string:
    return True
  else:
    return False

string = "Madam"
print("String:", string)
print("Is palindrome?", is_palindrome(string))
