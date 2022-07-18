from collections import deque
import sys
input=sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

def bfs(start):
    que = deque([start])
    visited[start] = True
    while que:

        cur = que.popleft()
        for next in edges[cur]:
            if not visited[next]:
                que.append(next)
                visited[next]=True


for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        ans += 1
print(ans)


