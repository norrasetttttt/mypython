def cl(nu):
    sum = 0
    for i in range(num):
        price = int(input("ราคาสินค้า : %d " % (i+1)))
        sum += price
    return sum

def tax(um):
    vat = um*7/100
    return vat

def disc(p):
    discount = p * 5/100
    return discount

def total(a,b,c):
    t = (a+b)-c
    return t

num = int(input("จำนวนสินค้า : " ))
su = cl(num)
print(" ราคารวม %.2f" % su)
print(" ลดราคา %.2f" % disc(su))
print(" ภาษี  %.2f" % tax(su))
print(" รวมราคา %.2f" % total(su, tax(su), disc(su)))