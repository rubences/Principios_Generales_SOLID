def print_matrix(matrix : List[List[int]]) -> None:
    """Prints out the matrix."""
    # check if the matrix is empty
    if len(matrix) == 0:
        # print out an empty matrix
        print("[]")
        # return
        return
    # create a list of strings
    strings : List[str] = []
    # loop through the rows
    for row in matrix:
        # create an empty string
        string = ""
        # loop through the columns
        for val in row:
            # add the value to the string
            string += str(val) + " "
        # add the string to the list of strings
        strings.append(string)
    # print out the list of strings
    print(strings)

# define a function that takes a list of lists
# and returns the transpose
def transpose(matrix : List[List[int]]) -> List[List[int]]:
    """Returns the transpose of the matrix."""
    # check if the matrix is empty
    if len(matrix) == 0:
        # return an empty matrix
        return []
    # create a new empty list
    new_matrix : List[List[int]] = []
    # loop through the rows
    for i in range(len(matrix[0])):
        # add the new row to the new matrix
        new_matrix.append(row_to_column(matrix, i))
    # return the new matrix
    return new_matrix

# define a function that takes a list of lists
# and returns the transpose
def row_to_column(matrix : List[List[int]], column : int) -> List[int]:
    """Returns the column of the matrix."""
    # create a new empty list
    new_row : List[int] = []
    # loop through the columns
    for row in matrix:
        # check if the row is long enough
        if len(row) <= column:
            # raise an error
            raise ValueError("Invalid matrix")
        # get the value at the current position
        val = row[column]
        # add it to the new row
        new_row.append(val)
    # return the new row
    return new_row

# define a function that takes a list of lists
# and returns the transpose
def transpose(matrix : List[List[int]]) -> List[List[int]]:
    # check if the matrix is empty
    if len(matrix) == 0:
        # return an empty matrix
        return []
    # create a new empty list
    new_matrix : List[List[int]] = []
    # loop through the rows
    for i in range(len(matrix[0])):
        # add the new row to the new matrix
        new_matrix.append(row_to_column(matrix, i))
    # return the new matrix
    return new_matrix

# define a function that takes a list of lists
# and returns the transpose
def row_to_column(matrix : List[List[int]], column : int) -> List[int]:
    # create a new empty list
    new_row : List[int] = []
    # loop through the columns
    for row in matrix:
        # check if the row is long enough
        if len(row) <= column:
            # raise an error
            raise ValueError("Invalid matrix")
        # get the value at the current position
        val = row[column]
        # add it to the new row
        new_row.append(val)
    # return the new row
    return new_row
# create a matrix
matrix : List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print it out
print_matrix(matrix)
# print out the transpose
print_matrix(transpose(matrix))