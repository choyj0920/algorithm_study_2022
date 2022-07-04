import sys
input=sys.stdin.readline
n=int(input())
arr =[list(input().rstrip()) for _ in range(n)]

def checkunion(size,row,col):
    k=arr[row][col]
    for r in range(row,row+size):
        for c in range(col,col+size):
            if arr[r][c] != k:
                return False
    return True

def solution(size,row,col):
    if size==1:
        print(arr[row][col],end='')
        return
    if checkunion(size,row,col): # 개체가 하나이면 모두 1이나 0으로 이루어져 있으면
        print(arr[row][col],end='')
        return

    else:
        print("(",end='')
        next_size=size//2
        solution(next_size,row,col)
        solution(next_size,row,col+next_size)
        solution(next_size,row+next_size,col)
        solution(next_size,row+next_size,col+next_size)
        print(")",end='')

solution(n,0,0)