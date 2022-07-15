import sys
#sys.stdin=open("C:/Users/ykkim/github/PYTHON/알고리즘 문제풀이/section 3/input.txt","rt")
n,m =map(int, input().split())
cnt=0
a = list(map(int, input().split()))
print(a)
for i in range(n):
    print(i)
    sum=0
    while(sum<m):
        sum+=a[i]
        i+=1
    if sum==m:
        cnt+=1