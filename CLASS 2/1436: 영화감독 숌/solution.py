def solution(n):
    number = 666

    counter = 0
    while True:
        if str(number).find('666') != -1:
            counter += 1

        if counter == n:
            break

        number += 1

    return str(number)


if __name__ == "__main__":
    n = int(input())
    answer = solution(n)
    print(answer)
