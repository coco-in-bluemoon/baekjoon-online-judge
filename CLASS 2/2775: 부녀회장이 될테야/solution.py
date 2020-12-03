def solution(floor, no):
    BASE = 0
    number_of_people = [[0] * (no+1) for _ in range(floor+1)]

    for f in range(floor+1):
        for n in range(1, no+1):

            if f == BASE:
                number_of_people[f][n] = n
            else:
                number_of_people[f][n] = sum(number_of_people[f-1][:n+1])

    return number_of_people[floor][no]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        floor = int(input())
        no = int(input())

        answer = solution(floor, no)
        print(answer)
