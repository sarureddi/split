t1,s1=map(int,input().split())
l1=list(map(int,input().split()))
if s1==11:
    print(min(l1))
elif s1==2:
    print(max(l1[0],l1[t1-1]))
else:
    print(max(l1))
