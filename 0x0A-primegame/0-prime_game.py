#!/usr/bin/python3
"""the 0-prime_game module
a prime game where players choose a prime number to
elminate all the factors from the list
the last person to make a move will win the game.
"""


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """determine the winner of the game for `x` rounds
    and `n` lists"""
    if not x or type(x) is not int:
        return
    if not nums or type(nums) is not list:
        return
    ben = 0
    maria = 0
    # make sure there no index out of range error
    rounds = x if x <= len(nums) else len(nums)
    for i in range(rounds):
        numbers = [num for num in range(1, nums[i] + 1)]
        # print(f"numbers: {numbers}")
        step = 0
        j = 0
        while j < len(numbers):
            # print(f"\tj: {j}")
            if is_prime(numbers[j]):
                # print(f"\t\tyes is_prime: {j}")
                current = numbers[j]
                step = step + 1
                factors = []
                multiplier = 1
                while True:
                    f = current * multiplier
                    if f > numbers[-1]:
                        break
                    factors.append(f)
                    multiplier = multiplier + 1
                if numbers.index(current) == j:
                    # print(f"\t\tTrue")
                    j = j - 1
                for factor in factors:
                    try:
                        numbers.remove(factor)
                    except ValueError:
                        continue
            j = j + 1
        if step == 0 or step % 2 == 0:
            ben = ben + 1
        elif step != 0 and step % 2 != 0:
            maria = maria + 1
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
