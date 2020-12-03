def solution(weight):
    answer = -1
    max_five = weight // 5

    for counter_five in range(max_five+1):
        remained_weight = weight - (5 * counter_five)
        if remained_weight % 3:
            continue

        counter_three = remained_weight // 3

        if answer == -1:
            answer = counter_three + counter_five
        else:
            answer = min(answer, counter_five + counter_three)

    return answer


if __name__ == "__main__":
    weight = int(input())
    answer = solution(weight)
    print(answer)
