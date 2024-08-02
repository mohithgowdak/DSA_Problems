def get_reverse_diagonal(matrix, start_row, start_col):
    diag_elements = []
    r, c = start_row, start_col
    while r < len(matrix) and c >= 0:
        diag_elements.append(matrix[r][c])
        r += 1
        c -= 1
    return diag_elements

def find_max_reverse_diagonal_sum(matrix):
    M = len(matrix)
    N = len(matrix[0])

    # Variables to track the maximum sum and corresponding diagonal
    max_sum = float('-inf')
    max_diag = []

    # Check diagonals starting from each column of the first row
    for start_col in range(N):
        diag = get_reverse_diagonal(matrix, 0, start_col)
        diag_sum = sum(diag)
        if diag_sum > max_sum:
            max_sum = diag_sum
            max_diag = diag

    # Check diagonals starting from each row of the last column
    for start_row in range(1, M):
        diag = get_reverse_diagonal(matrix, start_row, N - 1)
        diag_sum = sum(diag)
        if diag_sum > max_sum:
            max_sum = diag_sum
            max_diag = diag

    # Output the results
    print(max_sum)
    max_diag.sort(reverse=True)
    print(' '.join(map(str, max_diag)))

if __name__ == "__main__":
    # Example Input
    """
    Example Input:
    3 3
    1 2 3
    4 5 6
    7 8 9
    """

    # Read matrix dimensions
    M, N = map(int, input().split())
    
    # Read matrix
    matrix = [list(map(int, input().split())) for _ in range(M)]

    find_max_reverse_diagonal_sum(matrix)
