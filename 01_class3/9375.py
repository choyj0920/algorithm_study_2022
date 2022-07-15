import sys
input=sys.stdin.readline

for t in range(int(input())):
    arr=dict()
    for i in range(int(input())):
        name,category=input().split()
        if category in arr:
            arr[category]+=1 # +경우의 수
        else: # 처음 입력된 카테고리
            arr[category]=2     # 경우의 수 새로웃 의상 입거나 안입거나
    ans=1
    for key,value in arr.items():
        ans *=value
    print(ans-1)
