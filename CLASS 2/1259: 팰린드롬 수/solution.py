def solution(number):
    number = str(number)

    index_front = 0
    index_rear = len(number) - 1

    while index_front < index_rear:

        value_front = number[index_front]
        value_rear = number[index_rear]

        if value_front != value_rear:
            return 'no'

        index_front += 1
        index_rear -= 1

    return 'yes'


if __name__ == "__main__":
    while True:
        number = int(input())
        if number:
            answer = solution(number)
            print(answer)
        else:
            break
