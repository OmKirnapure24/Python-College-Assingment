def delete_element(lst, index):
  if index < 0 or index >= len(lst):
    print("Invalid index")
    return
  new_lst = lst[:index] + lst[index+1:]
  return new_lst

lst = [1, 2, 3, 4, 5]
index = 2
print("Original list:", lst)
print("Index to delete:", index)
print("New list:", delete_element(lst, index))
