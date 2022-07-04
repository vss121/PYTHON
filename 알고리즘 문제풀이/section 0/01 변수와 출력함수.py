'''
변수명 정하기
1. 영문, 숫자, _로 이루어진다
2. 대소문자 구분
3. 문자나 _로 시작
4. 특수문자 사용 X
5. 키워드 사용 X
'''
## 변수 확인
a=1
A=2
A1=3
#2b=4 error!
_b=4
print(a, A, A1, _b)
a, b, c=3, 2, 1
print(a, b, c)


##값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)


##변수 타입
a=12345
print(type(a))  #<class 'int'>
a=12.123456
print(type(a))  #<class 'float'> 8byte=64bit
a='student'
print(type(a))  #<class 'str'>


##출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep='')
print(a, b, c, sep='\n')
print(a, end=' ')
print(b, end=' ')
print(c)