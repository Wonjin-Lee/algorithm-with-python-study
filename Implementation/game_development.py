def solution(game_map, x, y, head):

    visited_count = 1
    game_map[y][x] = -1

    turn_left = {
        0 : 3,
        1 : 0,
        2 : 1,
        3 : 2
    }

    # 0 : 북, 1 : 동, 2 : 남, 3 : 서
    dx_front = [0, 1, 0, -1]
    dy_front = [-1, 0, 1, 0]
    dx_back = [0, -1, 0, 1]
    dy_back = [1, 0, -1, 0]

    turn_count = 0
    while True:
        # 좌측으로 90도 회전
        head = turn_left[head]
        turn_count += 1

        nx = x + dx_front[head]
        ny = y + dy_front[head]

        if game_map[ny][nx] == -1 or game_map[ny][nx] == 1:
            if turn_count < 4:
                # 방문 불가능하거나 방문한 곳이라면 그 상태로 1단계로 돌아감
                continue

            nx = x + dx_back[head]
            ny = y + dy_back[head]

            if game_map[ny][nx] == 1:
                return visited_count

        # 방문 가능하면서 아직 방문하지 않았다면 앞으로 한 칸 이동
        x = nx
        y = ny

        if game_map[y][x] == 0:
            game_map[y][x] = -1
            visited_count += 1

game_map = []
row, column = map(int, input().split())
y, x, head = map(int, input().split())
for _ in range(row):
    game_map.append(list(map(int, input().split())))

print(solution(game_map, x, y, head))