from collections import deque
n,k=map(int, input().split())
MAX_X=200001
dx = [[0,2],[1,1],[-1,1]]
visited=[0]*MAX_X

que=deque([n])
visited[n]=1
while que:
    cur =que.popleft()
    time=visited[cur]
    for dplus,dmultiple in dx:
        next=(cur+dplus)*dmultiple
        if 0 <= next < MAX_X  and visited[next]==0:
            que.append(next)
            visited[next]=time +1
            if next==k:

                que=[]
                break
print(visited[k]-1)
