def solution(adventurers):

    adventurers.sort()

    result = 0
    party_member_size = 0

    for adventurer in adventurers:
        party_member_size += 1

        if party_member_size >= adventurer:
            result += 1
            party_member_size = 0

    return result

adventurers = [2, 3, 1, 2, 2]

print(solution(adventurers))