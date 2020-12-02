def solution(target):
    answer = 0
    for number in range(1, target):
        digit_sum = sum([int(digit) for digit in str(number)])
        constructor_sum = number + digit_sum
        if constructor_sum == target:
            answer = number
            break
    return answer


if __name__ == "__main__":
    number = int(input())
    answer = solution(number)
    print(answer)
