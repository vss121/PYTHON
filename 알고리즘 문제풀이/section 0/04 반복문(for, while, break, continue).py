## range
a=range(10)
print(list(a))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

a=range(1,11)
print(list(a))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print()


for i in range(10):
    print("Hello")
    
for i in range(10,0,-1):
    print(i)
print()


i=1
while i<=10:
    print(i)
    i+=1
print()

i=10
while i>=1:
    print(i)
    i-=1
print()

while True:
    print(i)
    if i==10:
        break
    i+=1
print()

for i in range(1,11):
    if i%2==0:
        continue    # for문에 속해 있는 continue 밑의 부분을 지나감
    print(i)
print()

#for-else
for i in range(1,11):
    print(i)
    if i>15:
        break
else:   # (break없이) 정상적으로 종료되었을 경우
    print(11)