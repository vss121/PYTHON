import sys
sys.stdin=open("C:/Users/ykkim/github/PYTHON/알고리즘 문제풀이/section 2/input.txt","rt")

n = int(input())
a = list(map(int, input().split()))
tot = 0
cnt = 0

for x in a:
    if x==1:
        cnt+=1
    else:
        cnt=0
    tot += cnt
print(tot)
