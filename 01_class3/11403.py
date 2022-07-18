import sys
input =sys.stdin.readline
INF= int(1e9)  #무한을 의미하는 값으로 10억을 설정

def floydWarshall():
    # k = 거쳐가는 노드
    for k in range(n):
        # i= 출발 노드
        for i in range(n):
            # j = 도착 노드
            if edges[i][k] ==INF:
                continue
            for j in range(n):
                if edges[k][j] ==INF:
                    continue
                edges[i][j]=0


# 노드의 개수, 간선의 개수 입력
n= int(input())
# 경로 배열
edges=[[INF]*(n) for _ in range(n)]

for i in range(n): #같은 노선 다른 경로 존재
    temp=list(map(int,input().split()))
    for j in range(n):
        if temp[j]==1:
            edges[i][j]=0
for i in range(n):
    edges[i][i]=INF

floydWarshall()

# 값 출력
for i in range(n):
    for j in range(n):
        if edges[i][j] !=INF:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()