import sys
from collections import deque

input = sys.stdin.readline
close_d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
toblindness = {"R": "r", "r": "R", "B": 'b', 'b': "B", "G": 'r'}


def bfs(arr, row, col):
    n=len(arr)
    que = deque([(row, col)])
    check = arr[row][col]
    arr[row][col] = toblindness[check]
    while que:
        r,c=que.popleft()
        for dr,dc in close_d:
            n_r,n_c=r+dr , c+dc
            if 0<=n_r<n and 0<=n_c<n and arr[n_r][n_c]==check:
                arr[n_r][n_c] = toblindness[arr[n_r][n_c]]
                que.append((n_r,n_c))

if __name__ == '__main__':
    n = int(input())
    arr = [list(input().rstrip()) for _ in range(n)]
    ans=0
    for r in range(n):
        for c in range(n):
            if arr[r][c] in 'RGB':
                bfs(arr,r,c)
                ans+=1
    print(ans,end=' ')
    ans=0
    for r in range(n):
        for c in range(n):
            if arr[r][c] in 'rb':
                bfs(arr,r,c)
                ans+=1
    print(ans)
