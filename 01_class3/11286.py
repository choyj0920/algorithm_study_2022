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
            a,b =heapq.heappop(que)
            print(a*b)
    elif x<0:
        heapq.heappush(que,(-x,-1))
    else:
        heapq.heappush(que,(x,1))
