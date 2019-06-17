# O(nd) time | O(n) space
# where d is the number of denominations
def numberOfWaysToMakeChange(n, denoms):
    """
    ways[amount] += ways[amount - denomination]
    ways[amount] = ways[amount - denomination] + ways[amount]
    for amount - denomination >= 0
    base case: ways[amount=0] = number of ways for smallest demomination
    """
    ways = [0] * (n + 1)
    # Base case: the first coin has 1 way to represent the amount.
    ways[0] = 1

    for coin in denoms:
        amount = coin
        while amount < len(ways):

            # Since we set amount = coin, amount - coin is always equal
            # or greater than zero. Otherwise, check if amount - coin >= 0
            ways[amount] = ways[amount] + ways[amount-coin]
            amount += 1

    # print("Ways (i=amount) = {}".format(ways))
    print("Number of ways to change {} in terms of {} = {}".format(n, denoms, ways[n]))
    return ways[n]

if __name__ == "__main__":
    numberOfWaysToMakeChange(7, [2, 3, 4, 7])

