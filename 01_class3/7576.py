import sys
from collections import deque
input = sys.stdin.readline
close_d=[[-1,0],[1,0],[0,-1],[0,1]]

m,n=map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]

que=deque([])
cnt_unripe_to=0
for j in range(n):
    for k in range(m):
        if arr[j][k]==1:
            que.append((j,k))
        elif arr[j][k]==0:
            cnt_unripe_to+=1
ans=0
while que:
    j,k=que.popleft()
    days=arr[j][k]
    if cnt_unripe_to==0:
        break
    for dj,dk in close_d:
        next_j,next_k=j+dj,k+dk
        if  0 <=next_j <n and 0<=next_k<m and arr[next_j][next_k] ==0:
            cnt_unripe_to-=1
            arr[next_j][next_k]=days+1
            ans=days
            que.append((next_j,next_k))
if cnt_unripe_to==0:
    print(ans)
else:
    print(-1)
