def solution(warehouses):
    dp = [0] * 100

    dp[0] = warehouses[0]
    dp[1] = max(warehouses[0], warehouses[1])

    # Bottom-Up
    for i in range(2, len(warehouses)):
        dp[i] = max(dp[i - 1], dp[i - 2] + warehouses[i])

    return dp[len(warehouses) - 1]

warehouses = [1, 3, 1, 5]

print(solution(warehouses))