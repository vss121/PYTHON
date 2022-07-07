import sys
sys.stdin=open("C:/Users/ykkim/github/PYTHON/알고리즘 문제풀이/section 3/input.txt","rt")
arr = []
num = 0
yaksu = 0
s = input()
for i in s:
    if i.isnumeric():
        arr.append(i)

for j in range(len(arr)):
    num += int(arr[-1*(j+1)])*(10**j)

#print(arr)
print(num)

for k in range(1,num+1):
    if num%k==0:
        yaksu+=1

print(yaksu)