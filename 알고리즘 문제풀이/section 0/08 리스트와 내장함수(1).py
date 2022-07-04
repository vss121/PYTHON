import random as r
a = []  # empty list
b = list() # empty list

a=[1,2,3,4,5]
print(a[0])

b=list(range(1,11))
print(b)

c = a+b
print(c)

print(a)
a.append(6) # 마지막에 6 삽입
print(a)
a.insert(3,7)   # 3 index에 7을 삽입
print(a)
a.pop() # 마지막 원소 삭제
print(a)
a.pop(3) # 3 index 원소 삭제
print(a)
a.remove(4) # 특정 원소 삭제
print(a)

print(a.index(3))   # 해당 원소의 index 번호 반환

print(a)
print(sum(a))
print(max(a))
print(min(a))
print(min(7,5,3))

r.shuffle(a)    # 섞기
print(a)
a.sort()    # 오름차순
print(a)
a.sort(reverse=True)    # 내림차순
print(a)

a.clear()   # 리스트 원소 clear
print(a)