def solution(bowling_balls):

    count = 0

    for i in range(len(bowling_balls) - 1):
        for j in range(i + 1, len(bowling_balls)):
            first_ball = bowling_balls[i]
            second_ball = bowling_balls[j]

            if first_ball != second_ball:
                count += 1

    return count

def solution2(bowling_balls, ball_count, max_weight):

    balls = [0] * 11

    count = 0

    for x in bowling_balls:
        balls[x] += 1

    for i in range(1, max_weight + 1):
        ball_count -= balls[i]
        count += balls[i] * ball_count

    return count

bowling_balls = [1, 3, 2, 3, 2]
ball_count = 5
max_weight = 3
print(solution2(bowling_balls, ball_count, max_weight))