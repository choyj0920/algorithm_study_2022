import sys
input=sys.stdin.readline
n=int(input())
arr =[list(map(int,input().split())) for _ in range(n)]
ans=[0,0]
def checkunion(size,row,col): # 0 or 1 하나로만 이루어 져있는지 확인 함수
    k=arr[row][col]
    for r in range(row,row+size):
        for c in range(col,col+size):
            if arr[r][c] != k:
                return False
    return True

def solution(size,row,col):
    if size==1:
        ans[arr[row][col]]+=1
        return
    if checkunion(size,row,col): # 개체가 하나이면 모두 1이나 0으로 이루어져 있으면
        ans[arr[row][col]]+=1
        return
    else:
        next_size=size//2
        solution(next_size,row,col)
        solution(next_size,row,col+next_size)
        solution(next_size,row+next_size,col)
        solution(next_size,row+next_size,col+next_size)

solution(n,0,0)
for i in ans:
    print(i)