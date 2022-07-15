import sys
import heapq
input=sys.stdin.readline

que=[]

for i in range(int(input())):
    x=int(input())
    if x==0:
        if not que:
            print(0)
        else:
            print(-heapq.heappop(que))
    else:
        heapq.heappush(que,-x)
