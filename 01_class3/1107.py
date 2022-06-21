# baek1107 리모컨
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = input().split()
def have_broken(channel):
    set_ch=set(str(channel))
    for i in broken:
        if i in set_ch:
            return True

    return False

result = abs(n - 100)
for i in range(1000001):
    if not have_broken(i): result = min(result, len(str(i)) + abs(i - n))
print(result)

