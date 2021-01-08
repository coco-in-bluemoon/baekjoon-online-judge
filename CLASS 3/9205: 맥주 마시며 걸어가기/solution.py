from collections import deque


def calculate_distance(source, destination):
    return abs(source[0] - destination[0]) + abs(source[1] - destination[1])

def solution(home, drug_stores, festival):
    MAX_DISTANCE = 1000
    queue = deque([home])

    visited = [False] * len(drug_stores)

    while queue:
        x, y = queue.popleft()

        if calculate_distance((x, y), festival) <= MAX_DISTANCE:
            return 'happy'

        for index, drug_store in enumerate(drug_stores):
            if visited[index] or calculate_distance((x, y), drug_store) > MAX_DISTANCE:
                continue
            visited[index] = True
            queue.append(drug_store)

    return 'sad'


if __name__ == "__main__":
    num_test = int(input())
    for _ in range(num_test):
        num_drug_store = int(input())

        x, y = map(int, input().split())
        home = (x, y)

        drug_stores = list()
        for _ in range(num_drug_store):
            x, y = map(int, input().split())
            drug_stores.append((x, y))

        x, y = list(map(int, input().split()))
        festival = (x, y)

        answer = solution(home, drug_stores, festival)
        print(answer)
