import sys

input = sys.stdin.readline
n = int(input())
arr = [0] + [int(input()) for i in range(n)]
dp = [ [0, 0] for i in range(n+1)]
dp[1][1] = arr[1]
for i in range(0,n):
    # 한계단 오르기 - 무조건 i 계단에서 연속이 아니엿어야 해!
    dp[i+1][0]=max(dp[i][1]+arr[i+1], dp[i+1][0])
    # 두 계단 오르기 - i계단이 연속이엇든 아니였는 상관 x
    try:
        dp[i+2][1]=max(dp[i][1],dp[i][0])+arr[i+2]
    except:
        pass
print(max(dp[n]))


