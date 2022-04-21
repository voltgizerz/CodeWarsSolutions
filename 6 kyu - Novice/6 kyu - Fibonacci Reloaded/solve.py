def fib(n):
    dp = {0:0 , 1:1}
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n - 1]