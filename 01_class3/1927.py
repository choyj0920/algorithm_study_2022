import heapq
import sys

input = sys.stdin.readline
que = []
for i in range(int(input())):
    x = int(input())
    if x == 0:
        if len(que) ==0:
            print(0)
        else:
            print(heapq.heappop(que))
    else:
        heapq.heappush(que,x)