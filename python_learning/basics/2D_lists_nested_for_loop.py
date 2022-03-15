#! usr/bin/python3
print("Part 1 - 2D list")


number_grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [0]
]

print(number_grid[0][2])



print("Part 2 - nested for loop")

print("will print out number_grid rows")
for row in number_grid:
    print(row)

print("will print out number_grid rows")
for row in number_grid:
    for col in row:
        print(col)