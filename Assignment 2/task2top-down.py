def longest_walk(M):
    """
    this is the top-down DP solution for the task 1
    @param M: a matrix
    @return: the longest increasing walk
    @time complexity: O(N^2) where n is the size of the list
    @space complexity: O(N) where n is the size of the list
    """
    memo = ([[0]*len(M[0])])*len(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
            memo[i][j] = longest_walk_aux(M, i, j)
    return memo

def longest_walk_aux(M, i, j):
    """
    this function compute the longest walk ending at M[i][j] recursively
    @param M: a matrix
    @param i: the horizontal index
    @param j: the vertical index
    @return: the longest increasing walk ending at M[i][j]
    @time complexity: O(N^2) where n is the size of the list
    @space complexity: O(N) where n is the size of the list
    """
    valid = valid_walks(M, i, j)
    if valid == []:
        return 1
    else:
        previous = previous_walk(M, valid)
        return (1 + longest_walk_aux(M, previous[0], previous[1]))
    
def valid_walks(M, i, j):
    """
    this function compute the valid previous positions of the current position M[i][j]
    @param M: a matrix
    @param i: the horizontal index
    @param j: the vertical index
    @return: the valid previous positions of the current position M[i][j]
    @time complexity: O(1) due to there are maximum 9 adjencent element around the current position
    @space complexity: O(1) due to there can only be maximum 9 positions
    """
    adjacent = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
    valid = []
    for a in range(len(adjacent)):
        nextWalk = (i + adjacent[a][0], j + adjacent[a][1])
        if nextWalk[0] >= len(M) or (nextWalk[1] >= len(M[0])) or (nextWalk[0] < 0) or (nextWalk[1] < 0):
            continue
        if M[i][j] <= M[nextWalk[0]][nextWalk[1]]:
            continue
        else:
            valid.append(nextWalk)
    return valid

def previous_walk(M, valid):
    """
    this function compute the exact previous position of M[i][j] to achieve local longest walk
    @param M: a matrix
    @param valid: a array of tuple which holds all valid position
    @return: previous position of M[i][j] to achieve local longest walk represent in a tuple
    @time complexity: O(1) due to there are maximum 9 element in valid
    @space complexity: O(1) due to the value array has same length as valid
    """
    value = []
    for i in valid:
        walk = (M[i[0]][i[1]], i)
        value.append(walk)
    temp = value[0]
    for i in range(1, len(value)):
        if value[i][0] < temp[0]:
            temp = value[i]
    return (temp[1][0], temp[1][1])




M1 = [[1,2,3], [4,5,6], [7,8,9]]
M2 = [[4,6,5], [7,2,9], [1,3,6]]
M3 = [[1,2,3], [1,2,1]]


print(longest_walk(M3))