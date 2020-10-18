ac=int(input("Anul curent: ")) 
lc=int(input("Luna curenta: ")) 
zc=int(input("Ziua curenta: ")) 
an=int(input("Anul nasterii: ")) 
ln=int(input("Luna nasterii: ")) 
zn=int(input("Ziua nasterii: ")) 

if (ln==lc): 
    if ((zc>zn)or(zc==zn)): 
        print(ac-an,"ani") 
    else: 
        print((ac-an)-1,"ani") 
elif (lc>ln): 
    print(ac-an,"ani") 
else: 
    print((ac-an)-1,"ani")