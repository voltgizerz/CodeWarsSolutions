def fibonacci(n: int) -> int:
    dp = [0, 1] + [0] * n
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]