def circle(r):
    area = 22/7*pow(r,2)
    return area

r = float(input("radius: "))
print("พื้นที่วงกลม %.2f" % circle(r))