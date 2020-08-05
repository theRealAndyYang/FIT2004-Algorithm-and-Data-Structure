def longest_walk(M):
    """
    this is the top-down DP solution for the task 1
    @param M: a matrix
    @return: the longest increasing walk
    @time complexity: O(N^2) where n is the size of the list
    @space complexity: O(N) where n is the size of the list
    """
    if len(M) == 0:
        return 0
    if len(M) == 1 and len(M[0]) == 1:
        return M[0][0]

    memo = ([[0]*len(M[0])])*len(M)
    maxWalk = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            path = longest_walk_aux(M, i, j, memo)
            maxWalk = max(maxWalk, path)
    return maxWalk

def longest_walk_aux(M, i, j, memo):
    """
    this function compute the longest walk ending at M[i][j] recursively
    @param M: a matrix
    @param i: the horizontal index
    @param j: the vertical index
    @return: the longest increasing walk ending at M[i][j]
    @time complexity: O(N^2) where n is the size of the list
    @space complexity: O(N) where n is the size of the list
    """
    # valid = valid_walks(M, i, j)
    # if valid == []:
    #     return 1
    # else:
    #     previous = previous_walk(M, valid)
    #     return (1 + longest_walk_aux(M, previous[0], previous[1]))
    adjacent = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
    if memo[i][j] > 0:
        return memo[i][j]
    maxWalk = 0
    for a in range(len(adjacent)):
        r = i + adjacent[a][0]
        c = j + adjacent[a][1]
        if (not(valid(M, r, c))) or (M[r][c] <= M[i][j]):
            continue
        path = 1 + longest_walk_aux(M, r, c, memo)
        maxWalk = max(maxWalk, path)
    memo[i][j] = maxWalk
    return maxWalk

def valid(M, i, j):
    if (i >= len(M)) or (i < 0) or (j >= len(M[0])) or (j < 0):
        return False
    return True




M1 = [[1,2,3], [4,5,6], [7,8,9]]
M2 = [[4,6,5], [7,2,9], [1,3,6]]
M3 = [[1,2,3], [1,2,1]]


print(longest_walk(M1))

    