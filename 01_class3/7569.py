import sys
from collections import deque
input = sys.stdin.readline
close_d=[[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]

m,n,h=map(int,input().split())
arr =[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

que=deque([])
cnt_unripe_to=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k]==1:
                que.append((i,j,k))
            elif arr[i][j][k]==0:
                cnt_unripe_to+=1
ans=0
while que:
    i,j,k=que.popleft()
    days=arr[i][j][k]
    if cnt_unripe_to==0:

        break
    for di,dj,dk in close_d:
        next_i,next_j,next_k=i+di,j+dj,k+dk
        if 0<=next_i < h and 0 <=next_j <n and 0<=next_k<m and arr[next_i][next_j][next_k] ==0:
            cnt_unripe_to-=1
            arr[next_i][next_j][next_k]=days+1
            ans=days
            que.append((next_i,next_j,next_k))
if cnt_unripe_to==0:
    print(ans)
else:
    print(-1)
