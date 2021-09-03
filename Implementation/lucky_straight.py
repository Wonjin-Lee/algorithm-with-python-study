def solution(score):
    score = str(score)

    base_point = len(score) // 2

    left_score = sum(list(map(int, list(score[:base_point]))))
    right_score = sum(list(map(int, list(score[base_point:]))))

    return 'LUCKY' if (left_score == right_score) else 'READY'

score = 123402
score = 7755
print(solution(score))
