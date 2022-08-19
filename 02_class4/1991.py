import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

graph=dict()

ans=["","",""]
for i in range(int(input())):
    parent,left,right=input().split()
    if left ==".":
        left = None
    if right == ".":
        right =None
    graph[parent]=[left,right]

def search(curnode):
    # 전위순회
    ans[0]+=curnode

    left ,right =graph[curnode]
    if left!= None:
        search(left)

    ans[1]+=curnode

    if right != None:
        search(right)

    ans[2]+=curnode

search("A")

print(*ans,sep= "\n")

