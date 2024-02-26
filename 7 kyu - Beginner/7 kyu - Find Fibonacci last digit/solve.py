def get_last_digit(index):
    dp = {0:0 , 1:1}
    for i in range(2, index+1):
        dp[i] = dp[i-1] + dp[i-2]
    return int(str(dp[index])[-1])