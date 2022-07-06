import sys
sys.stdin=open("C:/Users/ykkim/github/PYTHON/알고리즘 문제풀이/section 3/input.txt","rt")

n = int(input())
for i in range(n):
    s=input()
    s = s.lower()
    size = len(s)
    for j in range(size//2):   # 문자열 안에서 문자를 직접 비교
        if s[j]!=s[-1-j]:   # list의 index 접근을 뒤부터 -1, -2, ...로도 가능
            print(f"#{i+1} NO") # print("#%d NO" % (i+1))
            break
    else:
        print(f"#{i+1} YES")