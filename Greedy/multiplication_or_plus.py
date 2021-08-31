def solution(numbers):
    list = [0, 2, 9, 8, 4]
    list.sort()

    is_first_multiplication = True

    plus = 0
    multiplication = 0

    for i in list:
        if i == 0 or i == 1:
            plus += i
            continue

        if is_first_multiplication is True:
            multiplication += i
            is_first_multiplication = False
            continue

        if is_first_multiplication is False:
            multiplication *= i

    return plus + multiplication

def solution2(numbers):

    result = int(numbers[0])

    for i in range(1, len(numbers)):
        number = int(numbers[i])
        if result <= 1 or number <= 1:
            result += number
        else:
            result *= number

    return result

numbers = '02984'

print(solution(numbers))
print(solution2(numbers))
