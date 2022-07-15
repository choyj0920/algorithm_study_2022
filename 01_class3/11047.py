import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n,k=map(int,input().split())
    arr=[int(input()) for  _ in range(n)]
    ans=0
    for i in range(1,n+1):
        ans += k//arr[-i]
        k %= arr[-i]
    print(ans)
