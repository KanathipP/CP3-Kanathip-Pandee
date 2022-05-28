def login():
    print("กรุณาเข้าสู่ระบบก่อนใช้บริการ")
    usernameInput = input("กรุณาใส่ Username:")
    passwordInput = input("กรุณาใส่ Password:")
    while usernameInput != "admin" or passwordInput != "1234" :
        print("มีข้อผิดพลาด Error")
        usernameInput = input("Username:")
        passwordInput = input("Password:")
    print("ล็อกอินสำเร็จ Login Succesful")
    return True
def showMenu():
    print("กรุณาเลือกโปรแกรมที่ต้องการครับ Select your program")
    print("(1) Vat Calculate")
    print("(2) Price Calculate")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice+totalPrice*vat/100
    return result
def priceCalculate():
    price1 = int(input("กรุณากรอกราคาสินค้าชิ้นที่ 1 First Product Price:"))
    price2 = int(input("กรุณากรอกราคาสินค้าชิ้นที่ 2 Second Product Price:"))
    return vatCalculate(price1+price2)

if login() == True:
    showMenu()
    if menuSelect() == 1 :
        priceInput = int(input("กรุณากรอกราคาสินค้า Price:"))
        print("ราคารวมทั้งหมด",vatCalculate(priceInput),"บาท ขอบคุณที่ใช้บริการครับ")
    else :
        print("ราคารวมทั้งหมด",priceCalculate(),"บาท ขอบคุณที่ใช้บริการครับ")

