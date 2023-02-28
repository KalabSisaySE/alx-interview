#!/usr/bin/python3
"""the 0-island_perimeter module
defines the function `island_perimeter`
"""


def island_perimeter(grid):
    """returns the perimeter of the island, if it exists in the grid"""
    # finding the first '1' or the edge of the island
    for row in grid:
        try:
            row.index(1)
            start_row = grid.index(row)
            break  # as soon as the first one is found
        except ValueError:
            continue

    if start_row:
        perimeter = 0
        for index, row in enumerate(grid[start_row:]):
            # if row does not contain any zeros
            # we have reached the end of the island
            # print(f'row: {row}')
            current_row = start_row + index
            try:
                row.index(1)
            except ValueError:
                return perimeter

            for current_col, elm in enumerate(row):
                if elm == 1:
                    # check top and bottom
                    if current_row >= 1:
                        if grid[current_row - 1][current_col] == 0:
                            perimeter = perimeter + 1
                    if current_row < len(grid) - 1:
                        if grid[current_row + 1][current_col] == 0:
                            perimeter = perimeter + 1
                    # check left and right
                    if current_col >= 1:
                        if grid[current_row][current_col - 1] == 0:
                            perimeter = perimeter + 1
                    if current_col < len(row) - 1:
                        if grid[current_row][current_col + 1] == 0:
                            perimeter = perimeter + 1
        return perimeter
    return 0
