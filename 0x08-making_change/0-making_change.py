#!/usr/bin/python3
"""the `0-making_change` module
defines the function `makeChange`
"""


def makeChange(coins, total):
    """returns the fewest number of coins to meet `total`"""
    if total < 0:
        return 0

    still_possible = True
    coins_collected = []
    coins.sort(reverse=True)

    while still_possible:
        for coin in coins:
            while sum(coins_collected) < total:
                coins_collected.append(coin)

            if sum(coins_collected) == total:
                return len(coins_collected)

            elif sum(coins_collected) > total:
                coins_collected.pop()

        if coins[-1] not in coins_collected:
            coins_collected.pop()
            for elm in set(coins_collected):
                if elm in coins:
                    coins.remove(elm)
        else:
            still_possible = False

    return -1
