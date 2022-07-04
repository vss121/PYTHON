a = input("숫자를 입력하세요 : ")
print(a)

a, b= input("숫자를 입력하세요 : ").split()
print(a+b)

a, b= map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# 형 변환
a = 4.3
b = 5
c=a+b
print(type(c))  # 실수형

