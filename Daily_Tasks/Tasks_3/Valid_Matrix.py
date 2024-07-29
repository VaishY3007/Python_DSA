def validateMatrix(matrix):
    if not matrix:
        return False 
    num_columns = len(matrix[0])
    for row in matrix:
        if len(row) != num_columns:
            return False  
    return True

# Function to take user input for a matrix
def inputMatrix():
    matrix = []
    while True:
        row = input("Enter a row (comma-separated values), or press Enter to finish: ")
        if row == "":
            break
        row = [int(val) for val in row.split(",")]
        matrix.append(row)
    return matrix

# Example usage:
print("Enter values for the matrix (press Enter on a blank line to finish):")
matrix = inputMatrix()
print("Matrix entered:", matrix)
print("Is the matrix valid?", validateMatrix(matrix))
