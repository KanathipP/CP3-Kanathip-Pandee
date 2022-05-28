menuList = []
priceList = []
def showBill():
    total = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        total = total+int(priceList[number])
    return total
while True:
    menuName = input("Enter your menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price:")
        menuList.append(menuName)
        priceList.append(menuPrice)
total = showBill()
print("Total %d" %(total))


