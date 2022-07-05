다시

- [ ] for-else 구문   
```
for i in range(1,11):
    print(i)
    if i>15:
        break
else:   # (break없이) 정상적으로 종료되었을 경우
    print(11)
```

- [ ] print   
```
for i in range(5):
    print('i:', i, sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()
```

- [ ] 5-i   
```
for i in range(5):
    for j in range(5-i):
        print('*', end=' ')
    print()
```

- [ ] 아스키숫자
- 문자 -> 아스키숫자   
print(ord('A')) #A는 65, Z는 90

- 아스키숫자 -> 문자   
print(chr(65))