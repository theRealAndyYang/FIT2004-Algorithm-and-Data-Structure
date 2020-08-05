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
            continue
        memo[-1] = current
    return (len(memo), memo)


print(longest_oscillation_demo([1,5,7,4,6,8,6,7,1]))

print(longest_oscillation_demo([1, 2]))