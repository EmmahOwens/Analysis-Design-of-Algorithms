def coinChange(coins, amount):
    # Edge case: amount is 0 requires 0 coins
    if amount == 0:
        return 0
    
    # Handle infinity case
    if amount == float('inf'):
        return -1
    
    # Initialize DP table with infinity (unreachable states)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    
    # Fill DP table
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:  # Check if the coin can contribute to the amount `i`
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result or -1 if no solution exists
    return dp[amount] if dp[amount] != float('inf') else -1

# Example 1: 
print(coinChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)

# Example 2: 
print(coinChange([2], 3))  # Output: -1 (No solution exists)

# Example 3: 
print(coinChange([1], 0))  # Output: 0 (Amount 0 requires 0 coins)

# Example 4: 
print(coinChange([1], float('inf')))  # Output: -1 (No solution exists)