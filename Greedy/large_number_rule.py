def sum_large_number(number_list, m, k):
    total = 0

    # 리스트를 역으로 정렬하여 인덱스 0번과 1번 값만 사용한다. (가장 큰 값, 두 번째로 큰 값)
    number_list = sorted(number_list, reverse=True)

    while True:
        # 가장 큰 값을 k번 더한다.
        for _ in range(k):
            total += number_list[0]
            m -= 1

            if m == 0:
                return total

        # 두 번째로 큰 값을 1번 더한다.
        total += number_list[1]
        m -= 1

        if m == 0:
            return total

number_list = [2, 4, 5, 4, 6]
print(sum_large_number(number_list, 8, 3))

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))