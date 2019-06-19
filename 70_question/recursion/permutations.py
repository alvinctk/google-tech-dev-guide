def getPermutations(array):
    if not array:
        return []
    solution = [[]]
    getPermutations_helper2(array, solution, 0, len(array))
    #print(solution)
    return solution

def getPermutations_helper(array, perm, solution):
    if not array:
        solution.append(perm)
        print(solution[-1])
        solution.append([])
        return
    for x in array:
        new_array = array - {x}
        perm.append(x)
        getPermutations_helper(new_array, perm, solution)
        perm.pop()

def getPermutations_helper2(array, solution, x, n):
    if x + 1 == n:
        solution.append(array[:])
        print(solution[-1])
        return
    i = x
    while i < n:
        array[i], array[x] = array[x], array[i]
        getPermutations_helper2(array, solution, x+1, n)
        array[i], array[x] = array[x], array[i]
        i += 1


getPermutations([1, 2, 3, 4])
