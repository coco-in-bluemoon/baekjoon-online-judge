from collections import deque


def solution(paranthesis):
    stack = deque([])
    for p in paranthesis:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return 'NO'
            stack.pop()
    return 'YES' if not stack else 'NO'


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        parenthesis = input().strip()
        answer = solution(parenthesis)
        print(answer)
