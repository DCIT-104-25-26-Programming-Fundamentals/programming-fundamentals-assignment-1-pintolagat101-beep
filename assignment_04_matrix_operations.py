# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# PART A - Transpose a Matrix

def read_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row_input = input("Enter row " + str(i + 1) + ": ")
        row_values = row_input.split()
        row = []
        for value in row_values:
            row.append(int(value))
        matrix.append(row)
    return matrix


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        result.append(new_row)
    return result


def print_matrix(matrix):
    for row in matrix:
        line = ""
        for value in row:
            line = line + str(value).rjust(4)
        print(line)


def main():
    print("Enter the original matrix:")
    matrix = read_matrix()

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    transposed = transpose_matrix(matrix)

    print("\nTransposed Matrix:")
    print_matrix(transposed)


main()

# PART B - Add Two Matrices

def read_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row_input = input("Enter row " + str(i + 1) + ": ")
        row_values = row_input.split()
        row = []
        for value in row_values:
            row.append(int(value))
        matrix.append(row)
    return matrix


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result


def print_matrix(matrix):
    for row in matrix:
        line = ""
        for value in row:
            line = line + str(value).rjust(4)
        print(line)


def main():
    print("Enter Matrix A:")
    matrix_a = read_matrix()

    print("Enter Matrix B (must be the same size as Matrix A):")
    matrix_b = read_matrix()

    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if rows_a != rows_b or cols_a != cols_b:
        print("Error: Matrix B must be the same size as Matrix A.")
        return

    sum_matrix = add_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    print_matrix(matrix_a)

    print("\nMatrix B:")
    print_matrix(matrix_b)

    print("\nSum (A + B):")
    print_matrix(sum_matrix)


main()
# PART C - Multiply Two Matrices

def read_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row_input = input("Enter row " + str(i + 1) + ": ")
        row_values = row_input.split()
        row = []
        for value in row_values:
            row.append(int(value))
        matrix.append(row)
    return matrix


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total = total + matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def print_matrix(matrix):
    for row in matrix:
        line = ""
        for value in row:
            line = line + str(value).rjust(4)
        print(line)


def main():
    print("Enter Matrix A:")
    matrix_a = read_matrix()

    print("Enter Matrix B (number of rows must equal number of columns in A):")
    matrix_b = read_matrix()

    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)

    if cols_a != rows_b:
        print("Error: Number of columns in A must equal number of rows in B.")
        return

    product = multiply_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    print_matrix(matrix_a)

    print("\nMatrix B:")
    print_matrix(matrix_b)

    print("\nProduct (A x B):")
    print_matrix(product)


main()
