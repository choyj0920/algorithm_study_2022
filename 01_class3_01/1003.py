# dp[n]= [0횟수, 1횟수]
dp=[[0,0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
for i in range(2,41):
    dp[i]=[dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]

for t in range(int(input())):
    print(*dp[int(input())])