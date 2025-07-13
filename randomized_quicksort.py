# Randomized Algorithms and Probabilistic Analysis
# Core Ideas:
# Randomness in Algorithems:
# 1. Introduce randomness to simplify algorithm design or avoid worst-case scenarios.
# 2. Monte Carlo vs Las Vegas:
# Monte Carlo algorithms have probabilistic accuracy, while Las Vegas algorithms always produce a correct result with probabilistic runtime
# Examples in practice:
# Randomized quicksort improves average performance.
# Probabilistic data structures like Bloom filters reduce memory consumption while tolerating a small error rate.
# Randomized quicksort chooses a random pivot each time to improve average-case performance.

import random

def randomized_quicksort(arr):
    """Sorts an array using the randomized quicksort algorithm"""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# Generate a random unsorted list
unsorted_array = [random.randint(1,100) for _ in range(10)]
print("Unsorted: ", unsorted_array)
print("\n")
print("Sorted: ",randomized_quicksort(unsorted_array))