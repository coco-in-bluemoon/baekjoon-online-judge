def solution(n):
    numbers = [str(number) for number in range(1, n+1)]
    return '\n'.join(numbers)


if __name__ == "__main__":
    n = 5
    answer = '1\n2\n3\n4\n5'
    assert solution(n) == answer

    n = int(input())
    my_answer = solution(n)
    print(my_answer)
