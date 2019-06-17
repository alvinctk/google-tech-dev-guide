def minNumberOfCoinsForChange(n, denoms):
    """
    nc = number_coins
    nc[i=amount] =  { min (nc[amount-coin] + 1 coin,
                            nc[amount])                   for i > 0,
                       0,                                 for i = 0
    """

    number_coins = [float('inf')] * (n + 1)
    number_coins[0] = 0

    for coin in denoms:

        # Since coin is always less than or equal to amount at the start
        # We don't need to compare each time within the loop
        amount = coin

        while amount < len(number_coins):
            # To compute the min number of coins to change at each amount
            number_coins[amount] = min(number_coins[amount-coin] + 1, number_coins[amount])
            amount += 1

    print("The minimum number of coins to change {} from {} = {}"
          .format(n, denoms, number_coins[n]))

    # Returns the min number of coins to change; Otherwise, return -1
    # when not found.
    return number_coins[n] if number_coins[n] != float('inf') else -1

if __name__ == "__main__":
    minNumberOfCoinsForChange(7, [1, 5, 10])

