from collections import deque


def solution(maze, x, y):

    count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    count += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))

    return maze[len(maze) - 1][len(maze[0]) - 1]


maze = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

print(solution(maze, 0, 0))