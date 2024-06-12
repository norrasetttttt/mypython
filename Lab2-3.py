x = float(input("น้ำหนัก  : "))
y = float(input("ส่วนสูง : "))
bmi = (x/(y/100)**2)
print("BMI : %.2f"%bmi)
if bmi < 18.49:
    print("น้ำหนักน้อย/ผอม")
elif bmi >= 18.5 and bmi <= 22.9:
    print("ปกติ(สุขภาพดี)")
elif bmi >=23 and bmi <= 24.9:
    print("อ้วน/โรคอ้วน1")
elif bmi >=25 and bmi <= 29.90:
    print("อ้วน/โรคอ้วน2")
else:
    print("อ้วน/โรคอ้วน3")