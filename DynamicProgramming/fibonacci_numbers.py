memo = [0] * 100

# Top-Down
def fibo(x):
    if x == 1 or x == 2:
        return 1

    if memo[x] != 0:
        return memo[x]

    memo[x] = fibo(x - 1) + fibo(x - 2)
    return memo[x]

print(fibo(99))

# Bottom-Up
memo[1] = 1
memo[2] = 1
n = 99

for i in range(3, n + 1):
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[n])