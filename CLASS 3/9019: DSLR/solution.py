# * L, R을 문자열 변환이 아닌 계산 식을 만드는 것이 관건
# * 문자열 연산은 최소화한다
# * 문제가 된 반례: 0 9999 : S


from collections import deque


def command_d(value):
    return (value * 2) % 10000

def command_s(value):
    return (value - 1) % 10000

def command_l(value):
    return (value % 1000) * 10 + (value // 1000)

def command_r(value):
    return (value % 10) * 1000 + (value // 10)

def operate_command(value, type):
    if type == 'D':
        return command_d(value)
    elif type == 'S':
        return command_s(value)
    elif type == 'L':
        return command_l(value)
    elif type == 'R':
        return command_r(value)

def solution(source, target):
    MAX_LIMIT = 10000

    commands = 'DSLR'

    visited = ['' for _ in range(MAX_LIMIT)]
    queue = deque([source])

    while queue:
        value = queue.popleft()
        command = visited[value]
        if value == target:
            break

        for type in commands:
            value_next = operate_command(value, type)
            if visited[value_next]:
                continue

            visited[value_next] = command + type
            if value_next == target:
                return visited[value_next]

            queue.append(value_next)

    return visited[target]


if __name__ == "__main__":
    assert solution(9999, 0) == 'DDLSLDDRDDDD'
    assert solution(0, 9999) == 'S'

    num_test = int(input())
    for _ in range(num_test):
        source, target = map(int, input().split())
        answer = solution(source, target)
        print(answer)

