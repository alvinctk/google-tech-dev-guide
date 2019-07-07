def knapsack(items, capacity, debug=None):
    values = [[0] * (capacity + 1) for _ in range(len(items)+1)]
    # values[i][j] =  max { values[i-1][j] if does not fit
    #                       values[i-1][j-w] + v if w < j

    rows, columns = len(values), len(values[0])
    for i in range(1, rows):
        value, weight = items[i-1]
        for j in range(1, columns):
            if weight <= j:
                values[i][j] = max(values[i-1][j], values[i-1][j-weight] + value)
            else:
                values[i][j] = values[i-1][j]

    if debug:
        for i in range(rows):
            print(values[i])

    i, j = rows - 1, columns - 1
    index = []

    while i > 0 and j > 0:
        if values[i][j] != values[i-1][j]:
            if values[i][j]:
                # Since index starts from 1, to rebase to indexed 0.
                index.append(i-1)
            i -= 1
            _, weight = items[i]
            j -= weight
        else:
            i -= 1
    index.sort()
    result = [values[-1][-1], index]
    print("knapsack({}, {}) = {}".format(items, capacity, result))
    return result

knapsack([[1,2], [4,3], [5, 6], [6, 7]], 10)
