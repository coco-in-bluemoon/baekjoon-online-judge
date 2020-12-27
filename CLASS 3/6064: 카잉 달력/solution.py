""" Note
1. 한 쪽(x)를 고정하고 나머지 쪽(y) 만을 고려한다
2. 숫자의 시작은 0이 아니라 1이다. → 나머지가 0이 나오는 경우 유의
"""

def calculate_gcd(a, b):
    if not b:
        return a
    return calculate_gcd(b, a % b)


def calculate_lcm(a, b):
    a, b = min(a, b), max(a, b)
    gcd = calculate_gcd(a, b)

    return gcd * (a // gcd) * (b // gcd)


def solution(m, n, x, y):
    counter = x
    y_current, y_target = x % n, y
    y_current = n if not y_current else y_current
    lcm = calculate_lcm(m, n)

    while y_current != y_target and counter <= lcm:
        counter += m
        y_current = (y_current + m) % n
        y_current = n if not y_current else y_current

    return counter if counter <= lcm else -1
    

if __name__ == "__main__":
    num_test = int(input())
    for _ in range(num_test):
        m, n, x, y = map(int, input().split())
        answer = solution(m, n, x, y)
        print(answer)

    # counterfeit
    assert solution(13, 11, 1, 11) == 66
