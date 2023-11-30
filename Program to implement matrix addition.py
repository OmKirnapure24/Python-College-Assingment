def matrix_addition(A, B):
  if len(A) != len(B) or len(A[0]) != len(B[0]):
    print("Invalid matrices")
    return
  C = []
  for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
      row.append(A[i][j] + B[i][j])
    C.append(row)
  return C
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print("Matrix A:", A)
print("Matrix B:", B)
print("Matrix A + B:", matrix_addition(A, B))
