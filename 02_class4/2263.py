import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n=int(input())
inorder=list(map(int,input().split()))
postorder=list(map(int,input().split()))

inorderindex= { value:index for index,value in enumerate(inorder)}


def solution(instart,inend,poststart,postend):
    # 일단 지금 위의 범위에 트리에서는 무조건! postorder의 마지막이 부모 노드일것
    # 그리고 프리오더에서는 이걸 가장 먼저 출력
    if instart>inend or postend<poststart:
        return
    root=postorder[postend]
    print(root,end=' ')

    # inorder에서 처음부터 ~ 부모노드 전까지 갯수가 좌측노드 갯수일것
    leftcount=inorderindex[root]-instart
    # inorder에서 부모 다음 노드부터 ~ 마지막 노드까지 갯수가 우측노드 갯수일것
    rightcount= inend -inorderindex[root]

    #좌측 트리 순회
    solution(instart,instart+leftcount-1,poststart,poststart+leftcount-1)
    #우측 트리 순회
    solution(inend-rightcount+1,inend,postend-rightcount,postend-1)

solution(0,n-1,0,n-1)





