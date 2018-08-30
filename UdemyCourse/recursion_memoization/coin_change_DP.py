# Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.
#
# For example:
# If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:
#
# 1+1+1+1+1+1+1+1+1+1
# 5 + 1+1+1+1+1
# 5+5
# 10
#
# With 1 coin being the minimum amount.

from rcviz import callgraph, viz


@viz
def coin_change(target, coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        for val in [coin for coin in coins if coin <= target]:
            total_coins = 1 + coin_change(target - val, coins)
            if min_coins > total_coins:
                min_coins = total_coins
    return min_coins


print(coin_change(10,[1,5]))
callgraph.render("coin_change_DP.png")


