n=int(input())
a=list()
for _ in range(n):
    a.append(int(input()))
a_set = set(a)

res=0
for x in a_set:
    cnt=1
    prev=a[0]
    '''
    for i in range(1,n):
        if a[i]!=x and a[i]==prev:
            cnt+=1
        if a[i]!=x and a[i]!=prev:
            prev=a[i]
            cnt=1  ###
        #print(cnt)'''
             
    for i in range(1,n):
        if x==a[i]:
            continue
        if prev==a[i]:
            cnt+=1
        else:
            prev=a[i]
            cnt=1
        
        if cnt>res:####
            res=cnt

    #print(cnt)

print(res)