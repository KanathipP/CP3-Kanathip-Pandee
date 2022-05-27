usernameInput = input("Username:")
passwordInput = input("Password:")
if usernameInput == "admin" and passwordInput == "1234" :
    print("Welcome to my shop!")
    print("(1) Happy Meal       :90  THB")
    print("(2) Yummy Yummt Set  :150 THB")
    print("(3) Supra Ultra Chikk:500 THB")
    userSelected = int(input(">>"))
    if userSelected == 1 :
        inputValue = int(input("How many do you want? >>"))
        print("Total:",90*inputValue,"THB")
        print("Enjoy your meal!")
    elif userSelected == 2:
        inputValue = int(input("How many do you want? >>"))
        print("Total:", 150 * inputValue, "THB")
        print("Enjoy your meal!")
    elif userSelected == 3 :
        inputValue = int(input("How many do you want? >>"))
        print("Total:",500*inputValue,"THB")
        print("Enjoy your meal!")
else :
    print("Error")
