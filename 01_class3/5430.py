from collections import deque
import sys
input=sys.stdin.readline

def calculator(arr,command):
    isreverse = False
    for c in command:
        if c == 'R':  # 뒤집기
            isreverse = not isreverse
        else:  # C연산
            try:
                if isreverse:  # 뒤집혀있으면 뒤에서 부터~
                    arr.pop()
                else:
                    arr.popleft()
            except:
                print('error')
                return
    if isreverse:
        arr.reverse()
    print(list(arr).__str__().replace(' ',''))

for t in range(int(input())):
    command=input().rstrip()
    n=int(input())
    try:
        arr= deque ([]+list(map(int,input().rstrip()[1:-1].split(','))))
    except:
        arr=[]
    calculator(arr,command)
