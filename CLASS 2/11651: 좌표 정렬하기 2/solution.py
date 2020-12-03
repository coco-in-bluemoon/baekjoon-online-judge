def solution(positions):
    return list(sorted(positions, key=lambda x: (x[1], x[0])))


if __name__ == "__main__":
    n = int(input())
    positions = list()
    for _ in range(n):
        positions.append(list(map(int, input().split())))

    answer = solution(positions)
    for x, y in answer:
        print('{:} {:}'.format(x, y))
