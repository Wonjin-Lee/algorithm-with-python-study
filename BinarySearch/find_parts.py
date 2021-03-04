def solution(parts_list, order_list):
    for part in order_list:
        result = binary_search(parts_list, part, 0, len(parts_list) - 1)

        if result is None:
            print('no', end=' ')
        else:
            print('yes', end=' ')


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
parts_list = list(map(int, input().split()))
parts_list.sort()

m = int(input())
order_list = list(map(int, input().split()))

solution(parts_list, order_list)

'''
    < 위 문제를 계수 정렬을 이용하여 해결한 코드 >
    
    parts_list = [0] * 100001
    
    # 가게에 있는 전체 부품 번호를 입력받아서 기록
    for i in input().split():
        parts_list[int(i)] = 1
        
    # 손님이 주문한 부품들을 리스트화
    order_list = list(map(int, input().split()))
    
    for part in order_list:
        if parts_list[part] == 1:
            print('yes', end=' ')
        else:
            print('no', end=' ')
'''

'''
    < 위 문제를 집합 자료형을 이용하여 해결한 코드 >
    
    # 가게에 있는 전체 부품 번호를 입력받아서 Set 자료형에 저장
    parts_list_set = set(map(int, input().split())
    
    # 손님이 주문한 부품들을 리스트화
    order_list = list(map(int, input().split()))
    
    for part in order_list:
        if part in parts_list_set:
            print('yes', end=' ')
        else:
            print('no', end=' ')
'''