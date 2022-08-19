import sys
input = sys.stdin.readline
v = int(input())
edges = [ [] for _ in range(v + 1)]
for i in range(1,v):
    parent,child,dis=map(int,input().split())
    edges[parent].append([child,dis])
    edges[child].append([parent,dis])
visited=[-1]*(v+1)

def dfs(cur, curdis):
    if visited[cur] != -1:
        return
    visited[cur] = curdis

    for next,dis in edges[cur]:
        dfs(next,curdis+dis)

# 임의의 1노드에서 dfs수행해서 가장 먼 노드 찾고
dfs(1,0)
maxnode=visited.index(max(visited))
# 그 노드를 기준으로 dfs다시
visited=[-1]*(v+1)
dfs(maxnode,0)

print(max(visited))
