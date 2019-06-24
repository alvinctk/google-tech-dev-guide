from collections import deque

def riverSizes(matrix):
    row, col = len(matrix), len(matrix[0])
    #seen = set()
    visited = [[False]*col for _ in range(row)]

    sizes = []

    i = j = 0
    for i in range(row):
        for j in range(col):
            #if (i * row + j) in seen:
            if visited[i][j]:
                continue
            else:
                print("\n i and j = ", i, j, sizes)
                find_river(i, j, matrix, row, col, visited, sizes)
    print("all sizes", sizes)
    return sizes

def find_river(i, j, matrix, row, col, visited, sizes):
    q = deque()
    q.append((i, j))
    current_size = 0
    k = 0
    print("find_river: i={} j={}".format(i, j))
    print("q={} seen={} sizes={}".format(q, visited, sizes))
    while q:
        i, j = q.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_size +=1
        print("Before getting nodes: q={} sizes={}".format(q, sizes))
        if i > 0 and not visited[i-1][j]:
            q.append((i-1, j))

        if i < row - 1 and not visited[i+1][j]:
            q.append((i+1, j))

        if j > 0 and not visited[i][j-1]:
            q.append((i, j-1))

        if j < col - 1 and not visited[i][j+1]:
            q.append((i, j+1))

        #get_node_to_vist(q, visited, i, j)
        print("After getting nodes: q={} sizes={}".format(q, sizes))
    if current_size > 0:
        sizes.append(current_size)
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            print(1 if visited[i][j] else 0, end=" ")
        print(end ="\n")

if __name__ == "__main__":
    """
    testInput = [
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    ]
    """
    testInput = [
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        ]
    expected = [1, 1, 2, 2, 5, 21]
    riverSizes(testInput)
