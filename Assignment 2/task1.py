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

print(longest_oscillation([1,5,7,4,6,8,6,7,1]))

print(longest_oscillation([10,9,1,8,1,8,8]))

print(longest_oscillation([1,1,1,1,1]))

print(longest_oscillation([1,2,3]))