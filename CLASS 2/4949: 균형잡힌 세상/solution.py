from collections import deque
import re


def is_valid_parenthesis(parenthesis):
    if not parenthesis:
        return True

    stack = deque([])
    for p in parenthesis:
        if p == '(' or p == '[':
            stack.append(p)
        else:
            if not stack:
                return False

            stack_top = stack.pop()
            if p == ')' and stack_top == '[':
                return False
            elif p == ']' and stack_top == '(':
                return False

    return True if not stack else False


def solution(sentence):
    pattern = r'[\[\]\(\)]'
    parenthesis = re.findall(pattern, sentence)
    return 'yes' if is_valid_parenthesis(parenthesis) else 'no'


if __name__ == "__main__":
    while True:
        line = input().rstrip()
        while not line.endswith('.'):
            line += input().rstrip()

        if line == '.':
            break

        answer = solution(line)
        print(answer)
