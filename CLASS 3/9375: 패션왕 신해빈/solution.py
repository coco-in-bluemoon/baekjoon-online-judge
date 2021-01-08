from collections import defaultdict


def solution(clothing):
    clothing_dict = defaultdict(set)
    for name, type in clothing:
        clothing_dict[type].add(name)

    counter = 1
    for type, names in clothing_dict.items():
        counter  *= (len(names) + 1)
    counter -= 1
    return counter


if __name__ == "__main__":
    num_test = int(input())
    for _ in range(num_test):
        num_clothing = int(input())
        clothing = list()
        for _ in range(num_clothing):
            clothing.append(input().split())
        answer = solution(clothing)
        print(answer)
