import sys
import heapq

input = sys.stdin.readline

for t in range(int(input())):
    minque, maxque = [], []
    k=int(input())
    visited=dict()
    for i in range(k):
        calcul, n = input().split()
        if calcul == 'I':
            heapq.heappush(maxque,(-int(n),i)) # -로 넣어 가장 큰값이 맨앞에있게
            heapq.heappush(minque,(int(n),i)) # + 로 넣어 가장 작은값이 맨앞에있게
            visited[i]=True
        elif n=='-1': # 최소 값 삭제 연산
            while minque and not visited[minque[0][1]]:
                # <-- minque가 비워져있지 않고 가장앞에있는게 이미 삭제된것이 아닐떄까지
                heapq.heappop(minque) # 다 삭제하고
            if minque:
                visited[minque[0][1]]=False
                heapq.heappop(minque) #맨 앞에있는 아직 삭제되지 않은 원소 하나 삭제
        else: # 최대 값 삭제 연산
            while maxque and not visited[maxque[0][1]]:
                # <-- maxque가 비워져있지 않고 가장앞에있는게 이미 삭제된것이 아닐떄까지
                heapq.heappop(maxque) # 다 삭제하고
            if maxque:
                visited[maxque[0][1]]=False
                heapq.heappop(maxque) #맨 앞에있는 아직 삭제되지 않은 원소 하나 삭제

    # 각 큐에 앞에있는 원소 중 이미 삭제되어 있는 것들 다 삭제 --
    while maxque and not visited[maxque[0][1]]: heapq.heappop(maxque)
    while minque and not visited[minque[0][1]]: heapq.heappop(minque)

    print(f"{-maxque[0][0]} {minque[0][0]}"if maxque and minque else "EMPTY")




