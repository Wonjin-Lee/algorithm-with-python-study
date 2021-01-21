def solution(n, k):
    count = 0

    while True:
        if n == 1:
            return count

        if n % k == 0:
            n //= k
            count += 1
            continue

        n -= 1
        count += 1

n, k = map(int, input().split())

print(solution(n, k))
