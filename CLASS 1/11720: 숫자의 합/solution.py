def solution(num_string):
    return sum([int(num) for num in num_string])


if __name__ == "__main__":
    n = int(input())
    num_string = input().strip()
    answer = solution(num_string)
    print(answer)
