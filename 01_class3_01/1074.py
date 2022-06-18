import sys
input= sys.stdin.readline
result = 0

def search(n, x, y):
    global result
    if x == r and y == c:
        print(int(result))
        exit(0)
    if n == 1:
        result += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        # r,c가 (x,x+n-1) , (y,y+n-1) 칸에 포함되지 않았으면
        # 현재 탐색 부분에 없으면
        result += n * n
        return
    # 현재 N x N 배열을 4분할 해서 N/2 x N/2  4개로 탐색
    search(n / 2, x, y)
    search(n / 2, x, y + n / 2)
    search(n / 2, x + n / 2, y)
    search(n / 2, x + n / 2, y + n / 2)


n, r, c = map(int, input().split(' '))
search(2 ** n, 0, 0)