import sys

input = sys.stdin.readline

n, m = int(input()), int(input())
s = input().rstrip()
i = 1  # ioi를 한번에 체크할꺼니 2번째 글자부터
cnt, ans = 0, 0
while i < m:
    if s[i - 1:i + 2] == 'IOI': # IOI임
        cnt += 1
        i+=1 # IOI가 한개 찾아졌으면 index를 두번 넘겨 확인 다다음자리에 IOI가 또있는지 확인
        if cnt == n:
            cnt -= 1
            ans += 1
    else: # IOI가 아님
        cnt=0
    i+=1
print(ans)
