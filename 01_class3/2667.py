import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

n= int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

def dfs(row, col):
    cnt=1
    que=deque([(row,col)])
    arr[row][col] = 0
    while que:
        currow, curcol = que.popleft()
        for i in range(4):
            nextrow = currow + dr[i]
            nextcol = curcol + dc[i]
            if 0 <= nextrow < n and 0 <= nextcol < n and arr[nextrow][nextcol] == 1:
                cnt+=1
                que.append((nextrow, nextcol))
                arr[nextrow][nextcol] = 0
    return cnt

ans=[]
for r in range(n):
    for c in range(n):
        if arr[r][c]==1:
            ans.append(dfs(r,c))
ans.sort()
print(len(ans))
for i in ans:
    print(i)