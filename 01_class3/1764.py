import sys
input=sys.stdin.readline
n,m=map(int,input().split())
no_Listen=set()
ans=[]
for i in range(n):
    no_Listen.add(input().rstrip())
for i in range(m):
    no_see = input().rstrip()
    if no_see in no_Listen:
        ans.append(no_see)
ans.sort()
print(len(ans))
for i in ans:
    print(i)