"""
5. Optimization Techniques:
 - Greedy Algorithms:
    Make the locally optimal choice at each stage with the hope of finding a global optimum.
 - Dynamic Programming:
    Break problems into subproblems that overlap, solving each just once and storing the results.
 - Branch and Bound:
    Systematically explore candidate solutions while eliminating those that cannot yield a better result.

Case Study- The Knapsack Problem:
 - A classical optimization problem where decisions must be made about including/excluding items to maximize value.

Efficiency Considarations:
 - Weighing trade-offs between computational spped and resource consumption.

A greedy algorithm for the coin change problem always selects the largest coin value possible.
Note that this method works optimally for many--but not all-- coin systems.

"""
def greedy_coin_change(amount, coins):
    """Returns a list of coins that add up to the amount using a greedy strategy.
    Assumes coins are sorted in descending order.
    """
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

# Coin denominations (sorted descending)
coins = [25, 10, 5, 1]
amount = 68 # for example, 68 cents
change = greedy_coin_change(amount, coins)
print("Coins used for 68 cents (greedy): ", change)