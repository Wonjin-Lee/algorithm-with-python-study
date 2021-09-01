def solution(coins):

    coins.sort()

    target = 1

    for coin in coins:
        if target < coin:
            break

        target += coin

    return target

# 1, 1, 2, 3, 9
coins = [3, 2, 1, 1, 9]

print(solution(coins))