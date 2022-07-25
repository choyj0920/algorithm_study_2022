import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dp=[[0,0,0] for i in range(n)]
dp[0]=arr[0]
for i in range(1,n):
    for j in range(3):
        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j-2])+arr[i][j]
print(min(dp[n-1]))
