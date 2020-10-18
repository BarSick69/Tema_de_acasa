#cate bile sunt in total
#care bile sunt mai multe,mari sau mici,si cate
#culoarea bilelor cele mai numeroase
rm=int(input())
am=int(input())
vm=int(input())
rmi=int(input())
ami=int(input())
vmi=int(input())
print(rm+am+vm+rmi+ami+vmi)
if(rm+am+vm>rmi+ami+vmi):
    print("mari ",rm+am+vm)
elif(rm+am+vm<rmi+ami+vmi):
    print("mici ",rmi+ami+vmi)
else:
    print("mari si mici ",rm+am+vm)
if(rm+rmi>am+ami and rm+rmi>vm+vmi):
    print("rosii: ",rm+rmi)
elif(am+ami>rm+rmi and am+ami>vm+vmi):
    print("albe: ",am+ami)
elif(vm+vmi>rm+rmi and vm+vmi>am+ami):
    print("verzi: ",vm+vmi)
elif(rm+rmi>am+ami and rm+rmi==vm+vmi):
    print("rosii si verzi: ",rm+rmi)
elif(rm+rmi>vm+vmi and rm+rmi==am+ami):
    print("rosii si albastre: ",rm+rmi)
elif(am+ami>rm+rmi and am+ami==vm+vmi):
    print("albastre si verzi: ",am+ami)
else:
    print("toate sunt la fel de multe:",am+ami)