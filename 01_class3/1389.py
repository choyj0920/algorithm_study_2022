from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)



def bfs(node):
    result = 0
    visited = [False] * (n + 1)
    que = deque([i])
    visited[node] = 1
    while que:
        curnode = que.popleft()
        curlevel = visited[curnode]
        for nextnode in edges[curnode]:
            if not visited[nextnode]:
                que.append(nextnode)
                visited[nextnode] = curlevel + 1
                result += curlevel # 실제 단계는 level-1
    return result

answer = -1
min_value = n * n
for i in range(1, n + 1):
    result=bfs(i)
    if min_value > result:
        min_value = result
        answer = i
print(answer)



