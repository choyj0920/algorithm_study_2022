import sys
input=sys.stdin.readline

n=int(input())
dp=[[0]*(n+1)for _ in range(n+1)]
for i in range(1,n+1):
    arr=[0]+list(map(int,input().split()))+[0]
    # 모두 index를 1이상으로 받아서-> 맨 앞칸 index=0칸은 안쓰니까
    # 맨 뒤에칸은 밑의 층의 가장 우측노드의 위층은 우측노드가 없으니까
    for j in range(1,i+1):
        dp[i][j]= arr[j]+ max(dp[i-1][j],dp[i-1][j-1]) # 위의 층의 두개중 선택
print(max(dp[n]))

