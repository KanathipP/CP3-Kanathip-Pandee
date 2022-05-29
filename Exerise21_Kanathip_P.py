from tkinter import *
import math
def leftClickButton(event):
    weight=float(textBoxWeight.get())
    height=float(textBoxHeight.get())
    BMI = weight/math.pow((height/100),2)
    result =""
    if BMI >=30:
        result ="อ้วนมาก"
    elif BMI>=25.5:
        result="อ้วน"
    elif BMI>=23.0:
        result="น้ำหนักเกิน"
    elif BMI>=18.6:
        result="น้ำหนักเหมาะสม"
    else : result="ผอม"
    labelResult.configure(text="%f %s" %(BMI,result))

def doubleClickButton(event):
    print("Double Click")

mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง(cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก(kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(mainWindow,text="ผลลัพธ์",width=20)
labelResult.grid(row=2,column=1)
mainWindow.mainloop()