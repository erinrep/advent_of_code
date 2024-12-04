import numpy as np

print("Day 3: Ceres Search")

with open("input.txt", encoding="utf-8") as f:
    lines = [list(x.replace("\n", "")) for x in list(f)]

string_to_find = "XMAS"

matrix = np.array(lines)

total = 0
for i, row in enumerate(matrix):
    # horizontal
    total += "".join(row).count(string_to_find)
    total += "".join(np.flip(row)).count(string_to_find)

    # vertical
    col = matrix[:, i]
    total += "".join(col).count(string_to_find)
    total += "".join(np.flip(col)).count(string_to_find)

rows, cols = matrix.shape
for i in range(-rows + len(string_to_find), cols - len(string_to_find) + 1):
    # diagonal top left to bottom right
    diag = np.diagonal(matrix, offset=i)
    total += "".join(diag).count(string_to_find)
    total += "".join(np.flip(diag)).count(string_to_find)

    # diagonal top right to bottom left
    diag = np.diagonal(np.rot90(matrix), offset=i)
    total += "".join(diag).count(string_to_find)
    total += "".join(np.flip(diag)).count(string_to_find)

print("Part 1:", total)


def get_element(matrix, x, y):
    if len(matrix) and x >= 0 and x < len(matrix[0]) and y >= 0 and y < len(matrix):
        return matrix[x][y]
    else:
        return None


total = 0
for x, row in enumerate(matrix):
    for y, letter in enumerate(row):
        if letter == "A":
            top_left = get_element(matrix, x - 1, y - 1)
            top_right = get_element(matrix, x + 1, y - 1)
            bottom_left = get_element(matrix, x - 1, y + 1)
            bottom_right = get_element(matrix, x + 1, y + 1)
            if (
                (top_left == "M" and bottom_right == "S")
                or (top_left == "S" and bottom_right == "M")
            ) and (
                (top_right == "S" and bottom_left == "M")
                or (top_right == "M" and bottom_left == "S")
            ):
                total += 1

print("Part 2:", total)
