import sys

input = sys.stdin.readline

maxDp = {"pre": [0, 0, 0], "cur": [0, 0, 0]}
minDp = {"pre": [0, 0, 0], "cur": [0, 0, 0]}
for i in range(int(input())):
    temp = list(map(int, input().split()))

    maxDp["cur"][0] = max(maxDp["pre"][0], maxDp["pre"][1]) + temp[0]
    minDp["cur"][0] = min(minDp["pre"][0], minDp["pre"][1]) + temp[0]

    maxDp["cur"][1] = max(maxDp["pre"]) + temp[1]
    minDp["cur"][1] = min(minDp["pre"]) + temp[1]

    maxDp["cur"][2] = max(maxDp["pre"][1], maxDp["pre"][2]) + temp[2]
    minDp["cur"][2] = min(minDp["pre"][1], minDp["pre"][2]) + temp[2]

    maxDp["pre"] = [*maxDp["cur"]]
    minDp["pre"] = [*minDp["cur"]]

print(max(maxDp["cur"]), min(minDp["cur"]))

