def calculate_gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def solution(a, b):
    a, b = max(a, b), min(a, b)
    gcd = calculate_gcd(a, b)
    lcm = gcd * (a // gcd) * (b // gcd)

    return [gcd, lcm]


if __name__ == "__main__":
    a, b = map(int, input().split())
    answer = solution(a, b)
    print('{}\n{}'.format(answer[0], answer[1]))
