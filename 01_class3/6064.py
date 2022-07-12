import sys

input = sys.stdin.readline


def solution(m, n, x, y):
    cur = x - y
    while cur + y <= m * n:
        if cur % n == 0:
            print(cur + y)
            return
        cur += m
    print(-1)

for t in range(int(input())):
    solution(*map(int, input().split()))

