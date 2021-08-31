import re

def solution(text):
    zero_count = len(list(filter(None, re.findall('0*', text))))
    one_count = len(list(filter(None, re.findall('1*', text))))

    return min(zero_count, one_count)

def solution2(text):

    zero_count = 0
    one_count = 0

    if text[0] == '0':
        zero_count += 1
    else:
        one_count += 1

    for i in range(len(text) - 1):
        if text[i] != text[i + 1]:
            if text[i + 1] == '0':
                zero_count += 1
            else:
                one_count += 1

    return min(zero_count, one_count)

text = '0001100'

print(solution(text))
print(solution2(text))