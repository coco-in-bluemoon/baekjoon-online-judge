def solution(participants, m, n):
    counter = 0
    for idx, participant in enumerate(participants):
        if participant:
            participants[idx] = max(0, participant - m)
            counter += 1

    for participant in participants:
        counter += (participant // n)
        counter += (1 if participant % n else 0)

    return counter


# # File Input
# if __name__ == "__main__":
#     filename = '삼성 SW 역량 테스트 기출 문제/inputs/시험 감독.txt'
#     f = open(filename, 'r')

#     T = int(f.readline())
#     for no in range(T):
#         f.readline()
#         f.readline()
#         participants = list(map(int, f.readline().split()))
#         m, n = map(int, f.readline().split())
#         answer = int(f.readline())

#         my_answer = solution(participants, m, n)
#         try:
#             assert answer == my_answer
#         except AssertionError:
#             print(f'{no+1}번 문제 틀림\t기댓값: {answer} 결과값: {my_answer}')

#     f.close()


# Standard Input
if __name__ == "__main__":
    input()
    participants = list(map(int, input().split()))
    m, n = map(int, input().split())
    my_answer = solution(participants, m, n)
    print(my_answer)
