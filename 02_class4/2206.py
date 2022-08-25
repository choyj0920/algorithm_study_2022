import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n,m=map(int,input().split())
graph = [ list(map(int,list(input().strip()))) for _ in range(n)]

dr=[0,0,-1,1]
dc=[-1,1,0,0]



def bfs():
    visited=[[[0 for dep in range(2)] for col in range(m)] for row in range(n)]
    visited[0][0][0]=1
    que= deque([[0,0,0]])

    while que:
        r,c,broken=que.popleft()

        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<m :
                if graph[nr][nc]==1 and broken==0 and visited[nr][nc][1]==0:
                    visited[nr][nc][1]=visited[r][c][0]+1
                    que.append([nr,nc,1])
                if graph[nr][nc]==0 and visited[nr][nc][broken]==0:
                    visited[nr][nc][broken]=visited[r][c][broken]+1
                    que.append([nr,nc,broken])

    return visited
nonbroken,broken=bfs()[n-1][m-1]
if(nonbroken==0 and broken==0):
    print(-1)
elif(nonbroken * broken == 0): # 둘중에하나 0
    print(max(nonbroken,broken))
else: # 둘다 0아님
    print(min(nonbroken,broken))








