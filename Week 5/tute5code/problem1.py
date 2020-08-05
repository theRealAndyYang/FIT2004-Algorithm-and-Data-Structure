
# bottom-up solution
def coin_change_bottomup(coins, value):
    min_coins = [0] + [None] * (value - 1)
    for v in range(1, value):
        if v < min(coins):
            pass
        else:
            options = []
            for i in range(len(coins)):
                if v >= coins[i]:
                    options.append(min_coins[v - coins[i]])
                    # residual = (v - coins[i]) + 1
                    # options = min_coins[0:residual]
            min_coins[v] = min(options) + 1
    return min_coins[value - 1]

#print(coin_change_bottomup([9, 6, 5, 1], 12))



# top-down solution
import math

def coin_change_topdown(coins, value):
    memo = [0] + [None] * (value - 1)
    return coin_change_topdown_aux(coins, value, memo)

def coin_change_topdown_aux(coins, value, memo):
    memo = [None] * value
    if value == 0:
        return 0
    if memo[value-1] == None:
        min_coins = math.inf
        for i in range(1, len(coins)):
            if coins[i] <= value:
                min_coins = min(min_coins, 1 + coin_change_topdown_aux(coins, value - coins[i], memo))
        memo[value-1] = min_coins
    return memo[value-1]

#print(coin_change_topdown([9, 6, 5, 1], 12))  