
n,m = map(int,input().split())
factorial=[1]*(n+1)
for i in range(1,n+1):
    factorial[i]=i*factorial[i-1]

print(factorial[n] // (factorial[m]*factorial[n-m]))