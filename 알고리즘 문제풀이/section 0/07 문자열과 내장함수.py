msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp = msg.upper()
print(tmp.find('T'))    # 1    # find()는 처음으로 발견된 index 번호를 return
print(tmp.count('T'))   # 2
print(msg[:2])  # slice
print(msg[3:5])
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

# 대문자만 출력
for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

# alphabet만 출력
for x in msg:
    if x.isalpha():
        print(x, end=' ')
print()

# 문자 -> 아스키숫자 
tmp = 'AZ'  #A는 65, Z는 90
for x in tmp:
    print(ord(x))

# 아스키숫자 -> 문자
tmp = 65
print(chr(tmp))