x = int(input("dati locul lui Ionel: "))
if (x <= 100):
    if (x % 4 == 0):
        print("Va primi un tricou negru")
    elif (x % 4 == 1):
        print("Va primi un tricou alb")
    elif (x % 4 == 2):
        print("Va primi un tricou rosu")
    elif (x % 4 == 3):
        print("Va primi un tricou albastru")
else:
    print("Ionel nu  este intre primii 100 si nu va primi premiu")