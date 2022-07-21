import sys
from collections import deque
input=sys.stdin.readline

dr=[0,0,-1,1]
dc=[-1,1,0,0]

MAX_DISTANCE=4000

def bfs(row,col): # 물고기들 찾기
    visited[row][col]=1 # visited[y][x] 도달하는데 걸리는시간+1
    que=deque([(row,col)])
    eatablefish = []
    mindis=MAX_DISTANCE
    while que:
        curr,curc=que.popleft()
        dis=visited[curr][curc]
        if mindis<dis-1: # 현재 찾은 가장 가까운 물고기보다 넓은 범위 탐색은 스킵
            continue
        for i in range(4):
            nr,nc=curr+dr[i],curc+dc[i]
            if 0<=nr<n and 0<=nc<n and visited[nr][nc] ==False:
                visited[nr][nc]=dis+1
                if arr[nr][nc]==0 or arr[nr][nc]==cursize:
                    que.append((nr,nc))
                elif arr[nr][nc]<cursize:
                    if mindis>=dis+1:
                        mindis=dis+1
                        eatablefish.append((nr,nc))
    return mindis,eatablefish

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    shark = [0, 0]
    leftfish=0
    cursize = 2
    eatcount = 0
    visited = []
    ans=0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                shark = [i, j]
                arr[i][j] = 0
            elif arr[i][j] != 0:
                leftfish+=1

    while leftfish>0:
        visited= [[False]*n for i in range(n)]
        dis,eatable=bfs(shark[0],shark[1])
        if dis==MAX_DISTANCE or eatable==[]:
            break
        ans +=dis-1
        eatable.sort()
        leftfish-=1
        r,c = eatable[0]
        shark=[r,c]
        arr[r][c]=0
        eatcount+=1
        if eatcount == cursize:
            cursize+=1
            eatcount=0
    print(ans)

