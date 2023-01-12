#!/usr/bin/python3
"""the `0-minoperations` module
defines the function `minoperations`
"""


def minOperations(n):
    """returns the minimum num of operations needed to reach `n` nums of `H`"""

    if n > 1:
        # Prime factorizing n to get the
        # optimal size before the last copy operation
        x = n
        prm_fctrs = []

        while x > 1:
            divisor: int = 2
            while x % divisor != 0:
                divisor += 1
            prm_fctrs.append(divisor)
            x = int(x / divisor)
        opt_size = prm_fctrs[-1]

        # calculate the number of operations
        num_operations = 0
        num_H = ["H"]

        # size to reach before the last copy
        while len(num_H) < opt_size:
            num_H.append("H")
            num_operations += 1
        num_operations += 1  # due to the fist Copy_All operation

        # after optimal size is reached
        copy = num_H.copy()
        while len(num_H) < n:
            num_H.extend(copy)
            num_operations += 1
        num_operations += 1  # due to the second Copy_All operation

        return num_operations

    return 0
