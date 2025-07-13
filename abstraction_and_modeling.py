# 4. Abstrction and Modeling in Problem Solving
""" Creating Models:
     - Convert real-world problems into mathematical models such as graphs, trees or state machines.
     - Identify primary components and ignore irrelevant details.

    Benefits of Abstraction:
     - Simplifies complex  systems into understandable structures.
     - Facilitates reuse of problem-solving strategies across different domains -
     for instance, applying similar techniques for both network routing and scheduling algorithms.

    Example
     - Memoization optimizes recursion by storing previous results. Here's the 
     Fibonacci sequence computed with a dynamic programming approach.
"""
def fibonacci_memo(n, memo={}):
    """ Compute the nth Fibonacci number using memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("Fibonacci numbers (with memoization): ")
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_memo(i)}")