from collections import deque
import heapq


def valid_move(position, snake, n):
    in_boundary = 0 <= position[0] < n and 0 <= position[1] < n
    self_eaten = position in snake
    return in_boundary and not self_eaten


def solution(n, apples, commands):
    board = [[0] * n for _ in range(n)]
    for r, c in apples:
        board[r-1][c-1] = 1

    heap = list()
    for t, command in commands:
        heapq.heappush(heap, (int(t), command))

    snake = deque([(0, 0)])
    position = (0, 0)
    direction = (0, 1)
    counter = 0

    while True:
        counter += 1
        position = (position[0] + direction[0], position[1] + direction[1])
        if not valid_move(position, snake, n):
            break
        snake.append(position)
        if not board[position[0]][position[1]]:
            snake.popleft()
        else:
            board[position[0]][position[1]] = 0

        if heap and heap[0][0] == counter:
            _, command = heapq.heappop(heap)
            if direction[0]:
                direction =\
                    (direction[1], direction[0])\
                    if command == 'L'\
                    else (-direction[1], -direction[0])
            elif direction[1]:
                direction =\
                    (direction[1], direction[0])\
                    if command == 'D'\
                    else (-direction[1], -direction[0])
    return counter


# File Input
if __name__ == "__main__":
    filename = './삼성 SW 역량 테스트 기출 문제/inputs/뱀.txt'
    f = open(filename, 'r')

    T = int(f.readline())
    for test in range(T):
        f.readline()

        N = int(f.readline())

        apples = list()
        a = int(f.readline())
        for _ in range(a):
            apple = list(map(int, f.readline().split()))
            apples.append(apple)

        commands = list()
        c = int(f.readline())
        for _ in range(c):
            command = f.readline().split()
            commands.append(command)

        answer = int(f.readline())

        my_answer = solution(N, apples, commands)

        try:
            assert answer == my_answer
        except AssertionError:
            print(f'{test+1}번 문제 오류\t기댓값: {answer} 결과값: {my_answer}')
    f.close()


# # Standard Input
# if __name__ == "__main__":
#     N = int(input())

#     apples = list()
#     a = int(input())
#     for _ in range(a):
#         apple = list(map(int, input().split()))
#         apples.append(apple)

#     commands = list()
#     c = int(input())
#     for _ in range(c):
#         command = input().split()
#         commands.append(command)

#     my_answer = solution(N, apples, commands)
#     print(my_answer)
