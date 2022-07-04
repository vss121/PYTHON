# 반복문을 이용한 문제 풀이
# 1. 1부터 N까지 홀수 출력하기
# 2. 1부터 N까지 합 구하기
# 3. N의 약수 출력하기


N = int(input())
print()

## 1
for i in range(1, N+1):
    if i%2==1:
        print(i)
print()

## 2
sum=0
for i in range(1, N+1):
    sum+=i
print(sum)
print()

## 3
for i in range(1, N+1):
    if N%i==0:
        print(i, end=' ')