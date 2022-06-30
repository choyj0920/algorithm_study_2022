import sys
input=sys.stdin.readline

n=int(input())
arr=[]
ans=[0,0,0]
def solution(size,row,col):
    if size==1: # 한칸 이면 바로 답으로
        ans[arr[row][col]+1]+=1
        return


    k=arr[row][col]
    # 한 종이인지 모두 같은 수를 가지고있는지 확인
    is_onepaper=True
    for r in range(size):
        if not is_onepaper :
            break
        for c in range(size):
            if arr[row+r][col+c] != k:
                is_onepaper=False
                break

    if is_onepaper: # 한 종이 이면 더하고 종료
        ans[k+1]+=1
        return 
    else: # 9개로 나누어 또 재귀 분할
        per_size =size//3
        for r in range(3):
            for c in range(3):
                solution(per_size,row+per_size*r,col+per_size*c)

for i in range(n):
    arr.append(list(map(int,input().split())))
solution(n,0,0)
for i in ans:
    print(i)