import sys

input = sys.stdin.readline
ss = input().replace('+', ' + ').replace('-', ' - ').split()
minus = False
ans = 0
for i in ss:
    if i == '-':
        minus = True
    elif i == '+':
        continue
    else:
        if minus:
            ans -= int(i)
        else:
            ans += int(i)
print(ans)