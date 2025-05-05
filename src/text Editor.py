from tkinter import *
import tkinter.filedialog

def saveas():
    global text  
    t = text.get("1.0", "end-1c")
    savelocation=tkinter.filedialog.asksaveasfilename()
    if (savelocation != ''):#Модификация проекта - обработка ошибок.
        file1=open(savelocation, "w+")
        file1.write(t)
        file1.close()

def FontHelvetica():
    text.config(font=("Helvetica", 12))

def FontBoldHelvetica():#Модернизация проекта - добавление жирного шрифта.
    text.config(font=("Helvetica", 12, "bold"))

def FontCourier():
    text.config(font=("Courier", 12))

def FontBoldCourier():
    text.config(font=("Courier", 12, "bold"))

root=Tk("Text Editor")
root.title("Text editor")#Модификация проекта - создание заголовка окна.
text=Text(root)
text.grid()

saveButton=Button(root, text="Save", command=saveas) 
saveButton.grid()

font=Menubutton(root, text="Font") 
font.grid() 
font.menu=Menu(font, tearoff=0) 
font["menu"]=font.menu
helvetica=IntVar() 
courier=IntVar()
boldHelvetica=IntVar()
boldCourier=IntVar()
font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)
font.menu.add_checkbutton(label="Bold Helvetica", variable=boldHelvetica, command=FontBoldHelvetica)
font.menu.add_checkbutton(label="Bold Courier", variable=boldCourier, command=FontBoldCourier)

root.mainloop()
