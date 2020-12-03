def solution(weight_height):
    grade = [1] * len(weight_height)

    for src_idx, src in enumerate(weight_height):
        for dst_idx, dst in enumerate(weight_height):
            if src_idx == dst_idx:
                continue

            src_weight, src_height = src
            dst_weight, dst_height = dst

            if (src_weight < dst_weight) and (src_height < dst_height):
                grade[src_idx] += 1

    return grade


if __name__ == "__main__":
    n = int(input())
    weight_height = list()
    for _ in range(n):
        weight_height.append(list(map(int, input().split())))
    answer = solution(weight_height)
    print(' '.join([str(grade) for grade in answer]))
