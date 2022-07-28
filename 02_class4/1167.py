import sys
input = sys.stdin.readline
v = int(input())
edges = [[] for _ in range(v + 1)]
for i in range(v):
    temp = list(map(int,input().split()))
    for j in range(1, len(temp)-1, +2):
        edges[temp[0]].append(temp[j:j + 2])
visited=[False]*(v+1)
maxnode,maxdis=1,0

def dfs(cur, curdis):
    global maxnode,maxdis
    if visited[cur] != False:
        return
    if maxdis<curdis:
        maxnode=cur
        maxdis=curdis

    visited[cur] = True

    for next,dis in edges[cur]:
        dfs(next,curdis+dis)

# 임의의 1노드에서 dfs수행해서 가장 먼 노드 찾고
dfs(1,0)
# 그 노드를 기준으로 dfs다시
visited=[False]*(v+1)
dfs(maxnode,0)

print(maxdis)
