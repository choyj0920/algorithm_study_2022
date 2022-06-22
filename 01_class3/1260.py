from collections import deque
import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
n, m, v = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(1, n + 1):
    edges[i].sort()

# dfs
visited = [0] * (n + 1)

def dfs(curnode):
    visited[curnode] = 1
    print(curnode,end=' ')
    for nextnode in edges[curnode]:
        if not visited[nextnode]:
            dfs(nextnode)
dfs(v)
print()

# bfs
visited = [0] * (n + 1)
def bfs(start):
    que=deque([start])
    visited[start]=1

    while que:
        curnode=que.popleft()
        print(curnode, end=' ')
        for nextnode in edges[curnode]:
            if not visited[nextnode]:
                que.append(nextnode)
                visited[nextnode]=1
    print()
bfs(v)
