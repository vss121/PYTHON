import sys
sys.stdin=open("C:/Users/ykkim/github/PYTHON/알고리즘 문제풀이/section 3/input.txt","rt")
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

c=a+b
c.sort()
print(c)