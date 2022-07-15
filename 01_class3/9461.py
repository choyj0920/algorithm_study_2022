import sys

input = sys.stdin.readline
arr = [0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 91
for i in range(6, 101):
    arr[i] = arr[i - 1] + arr[i - 5]

for t in range(int(input())):
    print(arr[int(input())])

