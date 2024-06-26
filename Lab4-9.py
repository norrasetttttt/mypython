def bmi(w,h):
    cal = weight/(height/100)**2
    return cal

weight = float(input("น้ำหนัก: "))
height = int(input("ส่วนสูง: "))
print ("BMI %.2f" % bmi(weight,height))

if bmi(weight,height) < 18.49:
    print("น้ำหนักน้อย/ผอม")
elif bmi(weight,height) >= 18.5 and bmi(weight,height) <= 22.9:
    print("ปกติ(สุขภาพดี)")
elif bmi(weight,height) >=23 and bmi(weight,height) <= 24.9:
    print("อ้วน/โรคอ้วน1")
elif bmi(weight,height) >=25 and bmi(weight,height) <= 29.90:
    print("อ้วน/โรคอ้วน2")
else:
    print("อ้วน/โรคอ้วน3")