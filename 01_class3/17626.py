import sys
input=sys.stdin.readline()
N = int(input())
dp = [4]*(N+1) #모든 자연수는 넷 혹은 그 이하의 제곱수 합으로 표현할수 있다했으므로 4로 초기화
dp[0]=0
dp[1]=1
for i in range(2, N+1):
    j = 1
    while (j**2) <= i:
        dp[i] = min(dp[i], dp[i - (j**2)] + 1)
        j += 1

print(dp[N])
