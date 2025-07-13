# Recurrences and Recursive Analysis
# Recurrence Relations: Used to express the time complexity of recursive algorithms
# Solving Methods: Utilizing the Master Theorem, iterative substitution, or generating functions
#  to simplify and solve recurrences.
# Aplications:
# Analyze divide-and-conquer algorithms(e.g., mergesort, quicksort)
#  Deduce the performance of recursive implementations.
# A classic recursive example is the Fibonacci sequence, which is defined by a recurrence relation.

def fibonacci_recursive(n):
    """Compute the nth Fibonacci number using simple recursion."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print("Fibonacci numbers (recursive): ")
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}") 