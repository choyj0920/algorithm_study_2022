n=int(input())
MOD =10007
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    try:
        dp[i]=dp[i-2]+dp[i-1]
    except:
        dp[i]=dp[i-1]
print(dp[n])