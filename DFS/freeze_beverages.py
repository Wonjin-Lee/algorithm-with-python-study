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

    if x < 0 or y < 0 or x >= max_x_size or y >= max_y_size:
        return

    if ice_frame[x][y] == 1:
        return

    # Visit point
    ice_frame[x][y] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        freeze(ice_frame, nx, ny)


ice_frame = [
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0]
]

print(solution(ice_frame))