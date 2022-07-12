import sys
sys.stdin=open("C:/Users/ykkim/github/PYTHON/알고리즘 문제풀이/section 3/input.txt","rt")
arr=list(range(21))
for _ in range(10):
    a,b= map(int, input().split())
    for i in range((b-a+1)//2):
        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]
a.pop(0)    # 0번 index를 pop
for x in arr:
    print(x, end=' ')