import sys

input = sys.stdin.readline
que = []
for i in range(int(input())):
    start, end = map(int, input().split())
    que.append((end, start))
que.sort()
ans=0 # 최대 회의 수
cur=0 # 회의실을 사용할 수 있는 가장 이른 시간
for end,start in que:
    if start>=cur:
        ans+=1
        cur=end
print(ans)