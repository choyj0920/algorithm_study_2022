import sys

input = sys.stdin.readline

dp =[0]*11
dp[0]=1
for i in range(0,11):
    try:
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
        dp[i+3] += dp[i]
    except:
        continue

for i in range(int(input())):
    print(dp[int(input())])
