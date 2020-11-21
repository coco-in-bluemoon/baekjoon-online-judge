def solution(n):
    numbers = [str(number) for number in range(n, 0, -1)]
    return '\n'.join(numbers)


if __name__ == "__main__":
    n = 5
    answer = '5\n4\n3\n2\n1'
    assert solution(n) == answer

    n = int(input())
    my_answer = solution(n)
    print(my_answer)
