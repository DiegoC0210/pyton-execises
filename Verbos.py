import os
os.system("clS")
v = input("registrar el verbo a conjugar: ")
l = len(v)
h =v[-2:l]
b = v[:l-2]
p = ["yo", "tu", "el/ella", "nosotros", "vosotros", "ellos"]
ar = ["o", "as", "a", "amos", "ais", "an"]
er = ["o", "es", "e", "emos", "eis", "en"]
ir = ["i", "es", "e","imos","is","en"]
if h == "ar":
    for i in range(len(p)):
        print(p[i],b+ar[i],"\n")
else:
    if h == "er":
        for i in range(len(p)):
            print(p[i],b+er[i],"\n")
    else:
        if h == "ir":
            for i in range(len(p)):
                print(p[i],b+ir[i],"\n")
