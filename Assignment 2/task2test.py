global memo = ([(0, 0)]*len(M[0])) * len(M)

def longest_walk(M):
    if len(M) == 0:
        return 0
    if len(M) == 1 and len(M[0]) == 1:
        return M[0][0]
    
    maxLen = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            pathLen = 1 + walk(M, i, j)
    return maxLen

def walk(M, i, j):
    adjacent = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
    if memo[i][j] > 0:
        return memo[i][j]
    maxLen = 0
    for a in range(len(adjacent)):
        r = i + adjacent[a][0]
        c = j + adjacent[a][1]
        if not(isSafe(M, r, c)) or (M[r][c] <= M[i][j]):
            continue
        pathLen = 1 + walk(M, r, c)
        maxLen = max(maxLen, pathLen)
    memo[i][j] = maxLen

def isSafe(M, i, j):
    if (i >= len(M)) or (i < 0) or (j >= len(M[0])) or (j < 0):
        return False
    return True


M1 = [[1,2,3], [4,5,6], [7,8,9]]
M2 = [[4,6,5], [7,2,9], [1,3,6]]
M3 = [[1,2,3], [1,2,1]]


print(longest_walk(M))