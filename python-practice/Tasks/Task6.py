def print_pyramid(row):
    if row <= 0:
        print("Invalid number of rows")
        return

    for i in range(1, row + 1):
        spaces = " " * (row - i)
        star = "*" * (2 * i - 1)
        print(spaces + star)


print_pyramid(4)