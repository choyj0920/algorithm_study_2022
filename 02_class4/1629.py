import sys
input = sys.stdin.readline

a,b,c=map(int,input().split())
ans=1
while b:
    if b%2:
        ans =ans*a % c
    b =b//2
    a= (a*a) % c
print(ans)