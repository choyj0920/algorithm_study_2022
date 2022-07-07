import sys
from collections import deque
input = sys.stdin.readline
n=int(input())
edges= [ [] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(int(input())):
    a,b =map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

que = deque([1])
ans=0
visited[1]=True
while que:
    cur = que.popleft()
    for next in edges[cur]:
        if not visited[next]:
            ans+=1
            que.append(next)
            visited[next]=True
print(ans)
