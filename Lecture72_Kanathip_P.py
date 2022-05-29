menuList = []

def showBill():
    total = 0
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],end=" ")
        print(menuList[number][1])
        total += int(menuList[number][1])
    print("Total:%d" %(total))
while True:
    menuName = input("Enter your menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price:")
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()



