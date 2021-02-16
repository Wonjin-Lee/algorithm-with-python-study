from collections import deque


def solution(ice_frame):
    count = 0

    for x in range(len(ice_frame)):
        for y in range(len(ice_frame[x])):
            if ice_frame[x][y] == 0:
                freeze(ice_frame, x, y)
                count += 1

    return count


def freeze(ice_frame, x, y):
    max_x_size = len(ice_frame)
    max_y_size = len(ice_frame[0])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([(x, y)])

    # Visit start point
    ice_frame[x][y] = 1

    while queue:
        current_location = queue.popleft()
        for i in range(4):
            nx = current_location[0] + dx[i]
            ny = current_location[1] + dy[i]

            if 0 <= nx < max_x_size and 0 <= ny < max_y_size:
                if ice_frame[nx][ny] == 0:
                    queue.append((nx, ny))
                    ice_frame[nx][ny] = 1


ice_frame = [
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0]
]

print(solution(ice_frame))
