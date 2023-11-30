def print_items(dict):
  
  for key in dict:
    print(key, ":", dict[key])

# Example
dict = {"name": "Alice", "age": 25, "gender": "female"}
print("Dictionary:", dict)
print("Items:")
print_items(dict)
