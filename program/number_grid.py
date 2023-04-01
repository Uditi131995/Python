# We are having a list within a list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# print(number_grid[row][column]): starting from zero
print(number_grid[0][0])
print(number_grid[0][1])


for row in number_grid:
    for column in row:
        print(column)
    print(row)
