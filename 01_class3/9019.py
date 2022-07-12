import sys

input = sys.stdin.readline

def calD(num):
    num*=2
    if num>9999:
        num %=10000
    return num

def calS(num):
    if num==0: return 9999
    return num-1
def calL(num):
    front = num%1000
    back=num // 1000
    return front*10+back

def calR(num):
    front=num % 10
    back=num // 10
    return front*1000 + back

dslr = [calD, calS, calL, calR]  # DSLR각각 함수 배열
str_dslr = "DSLR"

T = int(input())  # 테스트 케이스 갯수
while T > 0:
    dictPath = dict() # 각 값들의 경로 사전
    a, b = map(int, input().split())
    dictPath[a] = ''
    que = [a]
    while que:
        x = que.pop(0)
        path = dictPath[x]
        for i in range(4):
            next = dslr[i](x)
            if next not in dictPath:
                dictPath[next] = path + str_dslr[i]
                que.append(next)
                if next == b:
                    que = []
                    break
    print(dictPath[b])

    T -= 1
