import sys
input=sys.stdin.readline
arr=[False]*20
for _ in range(int(input())):
    s=input().rstrip()
    if s=='all':
        arr=[True]*20
    elif s=='empty':
        arr=[False]*20
    else:
        a,b = s.split()
        num=int(b)-1
        if a=='add':
            arr[num] = True
        elif a=='remove':
            arr[num]=False
        elif a=='check':
            print(1 if arr[num] else 0)
        else: # toggle
            arr[num] = not arr[num]
