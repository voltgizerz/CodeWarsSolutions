dp = {0:0 , 1:1}

def fibonacci(n):
    if n in dp:
        return dp[n]
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]