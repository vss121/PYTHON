import sys
sys.stdin=open("C:/Users/ykkim/github/PYTHON/알고리즘 문제풀이/section 3/input.txt","rt")
arr=[i for i in range(1,21)]
for i in range(10):
    a,b= map(int, input().split())
    arr[a-1:b]=sorted(arr[a-1:b],reverse=True)
    print(arr)

for x in arr:
    print(x, end=' ')


#sort와 sorted       