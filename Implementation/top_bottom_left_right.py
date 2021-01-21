def solution(map_size, tour_plan):
    current_location = [1, 1]

    for direction in tour_plan:
        if direction == "U":
            if current_location[0] > 1:
                current_location[0] -= 1

        if direction == "D":
            if current_location[0] < map_size:
                current_location[0] += 1

        if direction == "L":
            if current_location[1] > 1:
                current_location[1] -= 1

        if direction == "R":
            if current_location[1] < map_size:
                current_location[1] += 1

    return current_location

map_size = int(input())
tour_plan = list(input().split())

print(solution(map_size, tour_plan))

'''
    [ 다른 풀이 방식 ]
    
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['U', 'D', 'L', 'R']

for plan in tour_plan:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > map_size or ny > map_size:
        continue

    x, y = nx, ny    
'''


