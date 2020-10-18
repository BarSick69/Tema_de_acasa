n1=int(input())
n2=int(input())
n3=int(input())
if(n1>0 and n1<=10 and n2>0 and n2<+10 and n3>0 and n3<=10):
    if(n3<8):
        if(n2<n1):
            print(n1)
        elif(n1<n2):
            print(n2)
        else:
            print(n1,n2)
    elif(n3>=8):
        print(n1,n2,n3)
         
         
    
