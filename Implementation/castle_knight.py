def solution(current_location):

    dx = [-2, -2, 2, 2, 1, -1, 1, -1]
    dy = [1, -1, 1, -1, 2, 2, -2, -2]

    count = 0

    x = int(current_location[1])
    y = int(ord(current_location[0])) - int(ord('a')) + 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > 8 or ny > 8:
            continue

        count += 1

    return count

print(solution('a1'))

'''
x = int(current_location[1])
y = int(ord(current_location[0])) - int(ord('a')) + 1

count = 0

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

return count
'''