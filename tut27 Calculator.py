# Abhay
# Calculator

from tkinter import *


def input1(event):
    text = event.widget.cget("text")
    # print(text)

    if text == "=":
        try:
            # try evaluating the resulting str
            result = eval(str(value.get()))
            value.set(result)
        except Exception as e:
            # if failed its as error
            value.set("Error")
            print("error", e)
            # -------------------------------------DELETE----------------------------------
    elif text == "DEL":
        try:
            fullstring = value.get()
            # we are replacing the last string item[-1] with blank or ""
            # String slicing method
            newstring = fullstring.replace(fullstring[-1], "")
            value.set(newstring)

            # print(newstring)
            entry1.update()
        except Exception as e:
            print(e)

    elif text == "C":
        """"This will clear the screen"""
        value.set("")
        entry1.update()
    else:
        """if 1st input is 5, 2nd is 4 or + , both will be converted into string ie 54 or 5+"""
        value.set(value.get() + text)
        entry1.update()
        # print(value.get())


root = Tk()
root.geometry("430x550")
root.title("Calculator by Abhay")
value = StringVar()
entryframe = Frame(root, borderwidth=3, relief=SUNKEN)
entry1 = Entry(entryframe, font="lucida 27 bold", textvariable=value)
entry1.pack()
entryframe.pack(pady=20, padx=5)

buttonframe = Frame(root, )

list1 = ["9", "8", "7", "C", "6", "5", "4", "/", "3", "2", "1", "*", "00", "0", ".", "-", "%", "DEL", "=", "+"]
i = 0
for n in list1:
    # here width of button means 1 text width
    button1 = Button(buttonframe, text=n, font="lucida 20 ", padx=35, width=1, )
    button1.grid(row=int(i / 4), column=i % 4)
    i = i + 1

    button1.bind("<Button-1>", input1)

buttonframe.pack()

root.mainloop()
