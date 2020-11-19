def solution(height):
    star = list()
    for h in range(1, height+1):
        counter_blank = height - h
        counter_star = h

        star.append(f'{" "*counter_blank}{"*"*counter_star}')
    return '\n'.join(star)


if __name__ == "__main__":
    height = int(input())
    answer = solution(height)
    print(answer)
