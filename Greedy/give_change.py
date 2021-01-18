'''
동전을 가장 적게 사용하여 거스름돈을 건내 주었을 때의 리스트를 출력
'''

# 내가 작성한 코드
def get_change_list(amount):
    COIN_LIST = [500, 100, 50, 10]
    change_list = [0, 0, 0, 0]
    for i in range(4):
        count = amount // COIN_LIST[i]
        if count == 0:
            break

        amount -= (COIN_LIST[i] * count)
        change_list[i] += count

    return change_list

change_list = get_change_list(3680)

print(change_list)

'''
    아래 코드는 사용된 동전의 개수를 출력하는 문제의 답안이다.
    내가 작성한 코드와는 다르게 나머지(%)를 활용하여 총 금액을 줄여나갔다.

    n = 3680
    count = 0
    
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin
        n %= coin
        
    print(count)
'''