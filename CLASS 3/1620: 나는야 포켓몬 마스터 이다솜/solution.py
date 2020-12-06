def solution(poketmon, questions):
    poketmon_to_index = {p: str(idx + 1) for idx, p in enumerate(poketmon)}
    answers = list()
    for question in questions:
        if question.isdecimal():
            answers.append(poketmon[int(question) - 1])
        else:
            answers.append(poketmon_to_index[question])

    return answers


if __name__ == "__main__":
    num_poketmon, num_question = map(int, input().split())
    poketmon = list()
    for _ in range(num_poketmon):
        poketmon.append(input().strip())
    questions = list()
    for _ in range(num_question):
        questions.append(input().strip())

    answer = solution(poketmon, questions)
    print('\n'.join(answer))
