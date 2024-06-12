x = int(input("รับค่าคะแนน :  "))
if x > 100 or x < 0:
    print("กรุณาป้อนคะแนนใหม่")
elif x >= 80:
    print("เกรด A")
elif x >= 70 and x <80:
    print("เกรด B")
elif x >= 60 and x <70:
    print("เกรด C")
elif x >= 50 and x <60:
    print("เกรด D")
else:
    print("เกรด F")