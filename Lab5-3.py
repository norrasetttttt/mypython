def F(x):
    Fa = (9/5)*x+32
    return Fa

def K(x):
    Ke = x+273.15
    return Ke

c = int(input("องศาเซลเซี่ยส : "))
print("องศาฟาเรนไฮส์ : %.2f " % F(c))
print("องศาเคลวิน : %.2f " % K(c))