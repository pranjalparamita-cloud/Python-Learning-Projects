#Making a simple calculator using python GUI
from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry("400x600")
#root.resizable(False,False)
root.iconbitmap("calculator.ico")
root.config(bg="black")
def button_click(number):
    current=result_label.cget("text")
    if current==" ":
        result_label.config(text=str(number))
    else:
        result_label.config(text=current+str(number))
def button_clear():
    result_label.config(text=" ")
def button_add():
    global first_number
    global operation
    first_number=int(result_label.cget("text"))
    operation="addition"
    result_label.config(text=" ")
def button_subtract():
    global first_number
    global operation
    first_number=int(result_label.cget("text"))
    operation="subtraction"
    result_label.config(text=" ")
def button_multiply():
    global first_number
    global operation
    first_number=int(result_label.cget("text"))
    operation="multiplication"
    result_label.config(text=" ")
def button_divide():
    global first_number
    global operation
    first_number=int(result_label.cget("text"))
    operation="division"
    result_label.config(text=" ")
def button_equal():
    second_number=int(result_label.cget("text"))
    if operation=="addition":
        result=result_label.cget("text")
        result_label.config(text=str(first_number+second_number))
    elif operation=="subtraction":
        result=result_label.cget("text")
        result_label.config(text=str(first_number-second_number))
    elif operation=="multiplication":
        result=result_label.cget("text")
        result_label.config(text=str(first_number*second_number))
    elif operation=="division":
        if second_number==0:
            result_label.config(text="Error")
        else:
            result=result_label.cget("text")
            result_label.config(text=str(first_number/second_number))

result_label=Label(root,text=" ",font=("Arial",20,"bold"),bg="black",fg="white")
result_label.grid(row=0,column=0,columnspan=20,sticky='e',padx=10,pady=10)
result_label.config(font=("Verdana",20,"bold"),bg="black",fg="white")

add_button=Button(root,text="+",font=("Arial",14,'bold'),bg="lightgreen",fg="black",width=5,height=2,command=lambda:button_add())
add_button.grid(row=1,column=3,columnspan=20)
add_button.config(font=("Verdana",14,'bold'),bg="lightgreen",fg="black")
sub_button=Button(root,text="-",font=("Arial",14,'bold'),bg="lightgreen",fg="black",width=5,height=2,command=lambda:button_subtract())
sub_button.grid(row=2,column=3,columnspan=20)
sub_button.config(font=("Verdana",14,'bold'),bg="lightgreen",fg="black")
mul_button=Button(root,text="*",font=("Arial",14,'bold'),bg="lightgreen",fg="black",width=5,height=2,command=lambda:button_multiply())
mul_button.grid(row=3,column=3,columnspan=20)
mul_button.config(font=("Verdana",14,'bold'),bg="lightgreen",fg="black")
div_button=Button(root,text="/",font=("Arial",14,'bold'),bg="lightgreen",fg="black",width=5,height=2 ,command=lambda:button_divide())
div_button.grid(row=4,column=3,columnspan=20)
div_button.config(font=("Verdana",14,'bold'),bg="lightgreen",fg="black")

equal_button=Button(root,text="=",font=("Arial",14,'bold'),bg="lightgreen",fg="black",width=5,height=2,command=lambda:button_equal())
equal_button.grid(row=4,column=2,sticky='w',columnspan=20) 
equal_button.config(font=("Verdana",14,'bold'),bg="lightgreen",fg="black")

button1=Button(root,text="1",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(1))
button1.grid(row=3,column=0,columnspan=20)
button1.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button2=Button(root,text="2",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(2))
button2.grid(row=3,column=1,columnspan=20)
button2.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button3=Button(root,text="3",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(3))
button3.grid(row=3,column=2,columnspan=20)
button3.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button4=Button(root,text="4",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(4))
button4.grid(row=2,column=0,columnspan=20)
button4.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button5=Button(root,text="5",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(5))
button5.grid(row=2,column=1,columnspan=20)
button5.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button6=Button(root,text="6",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(6))
button6.grid(row=2,column=2,columnspan=20)
button6.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button7=Button(root,text="7",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(7))
button7.grid(row=1,column=0,columnspan=20)
button7.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button8=Button(root,text="8",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(8))
button8.grid(row=1,column=1,columnspan=20)
button8.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button9=Button(root,text="9",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(9))
button9.grid(row=1,column=2,columnspan=20)
button9.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
button0=Button(root,text="0",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=lambda:button_click(0))
button0.grid(row=4,column=1,columnspan=20)
button0.config(font=("Verdana",14,'bold'),bg="skyblue",fg="black")
clr_button=Button(root,text="C",font=("Arial",14),bg="skyblue",fg="black",width=5,height=2,command=button_clear)
clr_button.grid(row=4,column=0,columnspan=20)
clr_button.config(font=("Verdana",14,'bold'),bg="lightgreen",fg="black")

root.mainloop()