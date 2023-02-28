#!/usr/bin/python3
"""the 0-island_perimeter module
defines the function `island_perimeter`
"""


def island_perimeter(grid):
    """returns the perimeter of the island, if it exists in the grid"""
    # finding the first '1' or the edge of the island
    if grid and type(grid) is list and type(grid[0]) is list:
        start_row = -1
        for row in grid:
            try:
                row.index(1)
                start_row = grid.index(row)
                break  # as soon as the first one is found
            except ValueError:
                continue
        if start_row == -1:
            return 0  # there exists no island

        perimeter = 0
        for index, row in enumerate(grid[start_row:]):
            # if row does not contain any zeros
            # we have reached the end of the island
            curr_row = start_row + index
            try:
                row.index(1)
            except ValueError:
                return perimeter

            for curr_col, elm in enumerate(row):
                if elm == 1:
                    # check top and bottom
                    if curr_row >= 1:
                        if grid[curr_row - 1][curr_col] == 0:
                            perimeter = perimeter + 1
                    if curr_row < len(grid) - 1:
                        if grid[curr_row + 1][curr_col] == 0:
                            perimeter = perimeter + 1
                    # check left and right
                    if curr_col >= 1:
                        if grid[curr_row][curr_col - 1] == 0:
                            perimeter = perimeter + 1
                    if curr_col < len(row) - 1:
                        if grid[curr_row][curr_col + 1] == 0:
                            perimeter = perimeter + 1
                    
                    # if no more adjacent neighbors stop
                    if curr_row + 1 < len(grid) and curr_col + 1 < len(row):
                        right_is_zero = grid[curr_row][curr_col + 1] == 0
                        bottom_is_zero = grid[curr_row + 1][curr_col] == 0
                        if bottom_is_zero and right_is_zero:
                            break
        return perimeter

    return 0
