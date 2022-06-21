
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(graph,start):
    q= [start]

    graph[start[0]][start[1]] = 0

    while q:
        cur_node=q.pop(0)
        for d in range(4):
            ny=cur_node[0]+dx[d]
            nx=cur_node[1]+dy[d]
            if 0<=ny<n and 0<= nx <m and graph[ny][nx]==1:
                q.append((ny,nx))
                graph[ny][nx] = 0


for t in range(int(input())):
    m,n,k=map(int,input().split())
    field=[[0]*m for _ in range(n)]

    for i in range(k):
        x,y=map(int,input().split())
        field[y][x]=1
    ans = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] ==1:
                ans +=1
                bfs(field,(i,j))
    print(ans)






