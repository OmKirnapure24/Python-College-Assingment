def matrix_multiplication(A, B):
  if len(A[0]) != len(B):
    print("Invalid matrices")
    return
  C = []
  for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
      dot_product = 0
      for k in range(len(A[0])):
        dot_product += A[i][k] * B[k][j]
      row.append(dot_product)
    C.append(row)
  return C
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

print("Matrix A:", A)
print("Matrix B:", B)
print("Matrix A x B:", matrix_multiplication(A, B))
