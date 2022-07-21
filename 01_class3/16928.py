from collections import deque
START=1
DESTINATION=100

shortcut=dict()

def bfs():
    visited=[False]*(101)
    que=deque([START])
    visited[START]=0 # 어차피 START 칸으로 올 일 없음 ㅋ
    while que:
        cur=que.popleft()
        curcnt=visited[cur]
        for i in range(1,7):
            next=cur+i
            if START<next<=DESTINATION and visited[next]==False:
                visited[next]=curcnt+1
                if next in shortcut:
                    next=shortcut[next]
                    visited[next]=curcnt+1
                if next==DESTINATION:
                    print(curcnt+1)
                    return
                que.append(next)


if __name__ == '__main__':
    for i in range(sum(map(int,input().split()))):
        _to, _from =map(int,input().split())
        shortcut[_to]=_from
    bfs()


