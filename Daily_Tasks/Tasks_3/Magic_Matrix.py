def magic_matrix(n):
    if n % 2 == 0:
        raise ValueError("Magic Matrix is possible for only odd numbers")
    
    magic_square = [[0] * n for _ in range(n)]

    num =1 
    row, col = 0, n//2

    while num <= n * n:
        magic_square[row][col] = num
        num += 1
        
        new_row = (row -1) % n
        new_col = (col + 1) % n
        
        if magic_square[new_row][new_col] == 0:  
                row, col = new_row, new_col
        else:
            row = (row + 1) % n  # Move down one row
    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(str(cell).rjust(2) for cell in row))

n = int(input("Enter the value of number for valid matrix multiplication: "))
magic_square = magic_matrix(n)
print_magic_square(magic_square)
    