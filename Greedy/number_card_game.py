def best_card(card_board):
    best_card_number = 0
    for i in range(len(card_board)):
        min_number_in_row = sorted(card_board[i])[0]
        if min_number_in_row > best_card_number:
            best_card_number = min_number_in_row

    return best_card_number

# card_board = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
card_board = [[7, 3, 1, 8], [3, 3, 3, 4]]
print(best_card(card_board))

'''
    min(), max() 함수를 사용하는 방법을 사용했다면 숏코딩을 할 수 있었을 것이다.
    ex) min_number_in_row = min(card_board[i])
        best_card_number = max(min_number_in_row, best_card_number)
'''

n, m = map(int, input().split())

card_board = []
for i in range(n):
    card_board.append(list(map(int, input().split())))

print(card_board)