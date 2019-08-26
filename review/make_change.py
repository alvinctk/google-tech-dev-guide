def numberOfWaysToMakeChange(n, denoms):

    ways = [0] * (n+1)

    # Base case, since only 1 way to make 0 amount.
    # Helps to increment by 1 when the amount-i = 0 in ways[amount-i]
    ways[0] = 1

    for denom in denoms:

        print("before", denom, ways)
        amount = denom
        while amount < len(ways):
            # amount is always greater than or equal to denomination,
            ways[amount] = ways[amount] + ways[amount - denom]
            amount += 1
        print("after", denom, ways)
    return ways[n]

if __name__ == "__main__":
    numberOfWaysToMakeChange(6, [1, 5])
