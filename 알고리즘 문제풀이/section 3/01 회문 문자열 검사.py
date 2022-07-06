import sys
sys.stdin=open("C:/Users/ykkim/github/PYTHON/알고리즘 문제풀이/section 3/input.txt","rt")

n = int(input())
for i in range(n):
    s=input()
    s = s.lower()
    print(f"#{i+1}", end=' ')
    if s==s[::-1]:
        print("YES")
    else:
        print("NO")