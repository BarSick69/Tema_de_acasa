a=int(input())
s=int(input())
l=int(input())
n=a+s
if(a>=0 and s>=0 and l>=0):
    if(s>l):
        print(s)
    elif(s<l):
        print(l)
    else:
        print(s,l)
else:
    print(n)