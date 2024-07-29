def create_matrix(rows, columns, start):
    matrix = [[start + col + row * columns for col in range(columns)] for row in range(rows)]
    return matrix

def add_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None  # Matrices must have the same dimensions for addition
    result = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    return result

def sub_matrix(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None  # Matrices must have the same dimensions for subtraction
    result = [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    return result

def mul_matrix(a, b):
    if len(a[0]) != len(b):
        return None  # Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication
    result = [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
    return result

# Example usage:

rows_a = int(input("Enter the number of rows for matrix A: "))
columns_a = int(input("Enter the number of columns for matrix A: "))
start_a = int(input("Enter the starting value for matrix A: "))
matrix_a = create_matrix(rows_a, columns_a, start_a)

rows_b = int(input("Enter the number of rows for matrix B: "))
columns_b = int(input("Enter the number of columns for matrix B: "))
start_b = int(input("Enter the starting value for matrix B: "))
matrix_b = create_matrix(rows_b, columns_b, start_b)

print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

res_add = add_matrix(matrix_a, matrix_b)
res_sub = sub_matrix(matrix_a, matrix_b)
res_mul = mul_matrix(matrix_a, matrix_b)

print("\nMatrix A + Matrix B:")
if res_add:
    for row in res_add:
        print(row)
else:
    print("Matrices cannot be added due to different dimensions.")

print("\nMatrix A - Matrix B:")
if res_sub:
    for row in res_sub:
        print(row)
else:
    print("Matrices cannot be subtracted due to different dimensions.")

print("\nMatrix A * Matrix B:")
if res_mul:
    for row in res_mul:
        print(row)
else:
    print("Matrices cannot be multiplied due to incompatible dimensions.")
