def solution(width):
    dp = [0] * 1001

    dp[1] = 1
    dp[2] = 3

    for i in range(3, width + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

    return dp[width]

width = 3

print(solution(3))
