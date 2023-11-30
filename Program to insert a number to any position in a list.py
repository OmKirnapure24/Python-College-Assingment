def insert_number(lst, num, pos):
  if pos < 0 or pos > len(lst):
    print("Invalid position")
    return

  new_lst = lst[:pos] + [num] + lst[pos:]
  return new_lst

lst = [1, 2, 3, 4, 5]
num = 10
pos = 2
print("Original list:", lst)
print("Number to insert:", num)
print("Position to insert:", pos)
print("New list:", insert_number(lst, num, pos))
