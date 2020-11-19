def solution(height):
    star = list()
    for h in range(1, height+1):
        star.append('*' * h)
    return '\n'.join(star)


if __name__ == "__main__":
    height = int(input())
    answer = solution(height)
    print(answer)
