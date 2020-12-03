import sys


def solution():
    MAX_SIZE = 10000
    n = int(sys.stdin.readline())
    buckets = [0] * (MAX_SIZE + 1)

    for _ in range(n):
        number = int(sys.stdin.readline())
        buckets[number] += 1

    for bucket, frequency in enumerate(buckets):
        for _ in range(frequency):
            sys.stdout.write('{:}\n'.format(bucket))


if __name__ == "__main__":
    solution()
