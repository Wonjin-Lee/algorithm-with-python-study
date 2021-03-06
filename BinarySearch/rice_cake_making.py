def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0

        for i in array:
            if i > mid:
                total += i - mid

        if total < target:
            end = mid - 1
        else:
            start = mid + 1
            result = mid

    return result


n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

print(binary_search(array, m, start, end))
