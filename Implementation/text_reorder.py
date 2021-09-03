import re

def solution(text):
    pattern = re.compile('[A-Z]')
    alphabet = ''.join(sorted(pattern.findall(text)))

    pattern = re.compile('[0-9]')
    number = str(sum(list(map(int, pattern.findall(text)))))

    return alphabet + number

text = 'K1KA5CB7'
print(solution(text))