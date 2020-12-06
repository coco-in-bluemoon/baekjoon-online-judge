def solution(never_heard, never_seen):
    never_heard = set(never_heard)
    never_seen = set(never_seen)

    return sorted(list(never_heard & never_seen))


if __name__ == "__main__":
    never_heard = list()
    never_seen = list()

    n, m = map(int, input().split())
    for _ in range(n):
        never_heard.append(input().strip())
    for _ in range(m):
        never_seen.append(input().strip())

    answer = solution(never_heard, never_seen)
    print(len(answer))
    print('\n'.join(answer))
