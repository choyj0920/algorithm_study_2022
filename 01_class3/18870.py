import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
ziplist=list(sorted(set(arr)))
ziplist={ziplist[i]:i for i in range(len(ziplist))}
print(*[ziplist[i] for i in arr])