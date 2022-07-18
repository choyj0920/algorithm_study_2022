import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=0
for i in range(n):
    ans += (n-i)*arr[i]
print(ans)