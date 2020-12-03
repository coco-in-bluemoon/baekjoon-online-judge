def solution(members):
    member_informations = list()
    for idx, (age, name) in enumerate(members):
        member_informations.append((int(age), idx, name))

    member_informations = sorted(member_informations)

    answer = list()
    for age, _, name in member_informations:
        answer.append([str(age), name])

    return answer


if __name__ == "__main__":
    n = int(input())
    members = list()
    for _ in range(n):
        members.append(input().split())
    answer = solution(members)

    for member in answer:
        print(' '.join(member))
