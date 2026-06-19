# 5. Fibonacci Series (Recursive vs Iterative)
# This script demonstrates basic recursion, memoization, and iterative approaches.

def fib_recursive(n):
    """
    Computes the N-th Fibonacci number using recursion.
    Time Complexity: O(2^N) - Extremely slow for large N due to repeated subproblems
    Space Complexity: O(N) - Maximum recursion stack depth
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    """
    Computes the N-th Fibonacci number using iteration.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
        
    prev2 = 0
    prev1 = 1
    current = 0
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return current

def fib_memoization(n, memo={}):
    """
    Computes the N-th Fibonacci number using recursion + memoization (Dynamic Programming).
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

def main():
    print("--- Fibonacci Series ---")
    try:
        n = int(input("Enter index N for Fibonacci (e.g., 10): "))
    except ValueError:
        print("Invalid input, using default N = 10")
        n = 10
        
    print(f"Calculating the {n}-th Fibonacci number:")
    
    # 1. Iterative method (Safe and fast)
    iter_val = fib_iterative(n)
    print(f"Iterative Method O(N): {iter_val}")
    
    # 2. Dynamic Programming / Memoization (Fast, uses stack memory)
    memo_val = fib_memoization(n)
    print(f"Memoized Recursion O(N): {memo_val}")
    
    # 3. Naive Recursive method (Warning: O(2^N), slow for N > 30)
    if n <= 30:
        recur_val = fib_recursive(n)
        print(f"Naive Recursive Method O(2^N): {recur_val}")
    else:
        print("Skipping naive recursion as N is too large (would freeze execution).")

if __name__ == "__main__":
    main()
