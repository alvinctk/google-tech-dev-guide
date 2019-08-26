def minNumberOfCoinsForChange(n, denoms):
    num_coins = [float("inf")] * (n+1)
    num_coins[0] = 0

    for coin in denoms:
        amount = coin
        while amount <= n:
            num_coins[amount] = min(num_coins[amount], num_coins[amount-coin] + 1)
            amount += 1
    return num_coins[n] if num_coins[n] != float("inf") else -1
