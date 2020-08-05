##########     task 1    ##########

def longest_oscillation(L):
    """
    this is the bottom-up DP solution for the task 1
    @param L: a list
    @return: a tuple with the length if longest oscillation and the list of longest oscillation
    @time complexity: O(N^2) where n is the size of the list
    @space complexity: O(N) where n is the size of the list
    """
    n = len(L)
    memoIncrease = [1] * n  #len of longest oscillation from index 0 to i with last two element increasing
    memoDecrease = [1] * n  #len of longest oscillation from index 0 to i with last two element decreasing
    memo = [1] * n
    for i in range(n):
        for j in range(i):
            if (L[j] < L[i]) and (memoIncrease[i] < (memoDecrease[j] + 1)):
                memoIncrease[i] = memoDecrease[j] + 1
            elif (L[j] > L[i]) and (memoDecrease[i] < (memoIncrease[j] + 1)):
                memoDecrease[i] = memoIncrease[j] + 1
            else:
                pass
        memo[i] = max(memoIncrease[i], memoDecrease[i]) # update memo by identifying the maximum len of oscillation from 0 to i
    ### the algorithm has finished creating memo array ###

    # construct the longest oscillation using memo
    lgs_osl = []
    for i in range(n):
        try:
            if memo[i+1] > memo[i]:
                lgs_osl.append(L[i])
        except IndexError:
            lgs_osl.append(L[i])

    return (max(memo), lgs_osl)

def longest_oscillation_optimize(L):
    """
    this is the bottom-up DP solution for the task 1
    @param L: L list
    @return: L tuple with the length if longest oscillation and the list of longest oscillation
    @time complexity: O(N) where n is the size of the list
    @space complexity: O(N) where n is the size of the list
    """
    if L == []: 
        return []
    memo = [L[0]]
    try:
        memo.append(L[1])
    except IndexError:
        return (1, L)
    for current in L[1:]:
        if len(memo) == 1:
            memo.append(current)
            continue
        # We need to see if the current is the local maximum/minimum depending on the current trend. 
        # Indicate this using signs.
        # Show the current trend by substracting the second-last element from last element, 
        # if positive, the next element should be smaller, otherwise it should be greater
        # If the current element is greater than the last element in memo and this one should be
        # greater according to the trend, the equation will be negative and append this to memom
        # Otherwise the current element is the new local extreme, so we replace it with the last
        # element in the memo
        if (current - memo[-1]) * (memo[-1] - memo[-2]) < 0:
            memo.append(current)
            continue    # go to next iteration without replacing anything if we append the current element
        memo[-1] = current
    return (len(memo), memo)






##########     task 2    ##########

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