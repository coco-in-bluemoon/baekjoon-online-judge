def solution(numbers):
    NUM_DIGIT = 10

    product = 1
    for number in numbers:
        product *= number

    product_str = str(product)
    answer = [0] * NUM_DIGIT
    for number in product_str:
        answer[int(number)] += 1

    return answer


if __name__ == "__main__":
    numbers = [150, 266, 427]
    assert solution(numbers) == [3, 1, 0, 2, 0, 0, 0, 2, 0, 0]

    numbers = list()
    for _ in range(3):
        numbers.append(int(input()))
    answer = solution(numbers)
    print('\n'.join([str(number) for number in answer]))