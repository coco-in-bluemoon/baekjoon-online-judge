'''Note
모든 항을 다 빼주는 것이 최소
'''


def solution(expression):
    minus_terms = expression.split('-')
    first_term = minus_terms[0]
    answer = sum(list(map(int, first_term.split('+'))))
    for term in minus_terms[1:]:
        answer -= sum(list(map(int, term.split('+'))))
    return answer


if __name__ == "__main__":
    expression = '55-50+40'
    assert solution(expression) == -35

    expression = input().strip()
    answer = solution(expression)
    print(answer)
