import sys
from collections import deque
input=sys.stdin.readline

dr=[0,0,-1,1]
dc=[-1,1,0,0]

n,m=map(int,input().split())
arr =[list(map(int,list(input().rstrip()))) for _ in range(n)]

que=deque([(0,0)])
arr[0][0]=2
while que:
    currow,curcol =que.popleft()
    curcnt=arr[currow][curcol]
    for i in range(4):
        nextrow=currow+dr[i]
        nextcol=curcol+dc[i]
        if 0<=nextrow<n and 0<=nextcol<m and arr[nextrow][nextcol]==1:
            que.append((nextrow,nextcol))
            arr[nextrow][nextcol] = curcnt+1
            if nextrow==n-1 and nextcol==m-1:
                print(curcnt)
                exit(0)