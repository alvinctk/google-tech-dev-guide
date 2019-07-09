def maxProfitWithKTransactions(prices, k):
    n = len(prices)
    profit = [[0]*n for _ in range(k+1)]

    """
    t := number of transactions
    d := day at which either buy/sell stock

    profit[t][d] = max ( previous day profit = profit[t][d-1] ,

                         profit sold at this day + max(buy for this transaction + profit at last transaction)
                         prices[d] + max(-prices[x] + profit[t-1][x], where 0 <= x < d)
    """
    if not prices:
        return 0

    for t in range(1, k+1):
        for d in range(1, n):
            previous_day_profit = profit[t][d-1]
            max_profit_buy_on_t = float("-inf")
            for x in range(0, d):
                max_profit_buy_on_t = max(max_profit_buy_on_t, -prices[x] + profit[t-1][x])

            profit[t][d] = max(previous_day_profit, prices[d] + max_profit_buy_on_t)
    debug = False
    if debug:
        print(prices)
        for row in profit:
            print(row)

    print("Maximum profit for k={} transaction for {} stock prices at each day = {}".format(k, prices, profit[-1][-1] if profit else 0))
    return profit[-1][-1]

if __name__ == "__main__":
    maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2)



