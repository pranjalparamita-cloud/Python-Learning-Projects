n=int(input("                                                              Enter number of numbers to calculate upto 9: "))
m=int(input("What operation to do: \n 1.Multiplication \n 2.Division \n 3.Subtraction \n 4.Addition \n"))
if(n==0):
    print("0 number selected \n No value inserted")
elif(n==1):
    a=int(input("Enter 1 number:"))
    if(m==1):
        print("The multiplication is: ",a)
    elif(m==2):
        print("The division is: ",a)
    elif(m==3):
        print("The subtraction is: ",a)
    elif(m==4):
        print("The addition is: ",a)
    else:
        print("Error")
elif(n==2):
    a=int(input("Enter 1 number:"))
    b=int(input("Enter 2 number:"))
    if(m==1):
        print("The multiplication is: ",a*b)
    elif(m==2):
        print("The division is: ",a/b)
    elif(m==3):
        print("The subtraction is: ",a-b)
    elif(m==4):
        print("The addition is: ",a+b)
    else:
        print("Error")
elif(n==3):
    a=int(input("Enter 1 number:"))
    b=int(input("Enter 2 number:"))
    c=int(input("Enter 3 number:"))
    if(m==1):
        print("The multiplication is: ",(a*b)*c)
    elif(m==2):
        print("The division is: ",(a/b)/c)
    elif(m==3):
        print("The subtraction is: ",(a-b)-c)
    elif(m==4):
        print("The addition is: ",(a+b)+c)
    else:
        print("Error")
elif(n==4):
    a=int(input("Enter 1 number:"))
    b=int(input("Enter 2 number:"))
    c=int(input("Enter 3 number:"))
    d=int(input("Enter 4 number:"))
    if(m==1):
        print("The multiplication is: ",((a*b)*c)*d)
    elif(m==2):
        print("The division is: ",((a/b)/c)/d)
    elif(m==3):
        print("The subtraction is: ",((a-b)-c)-d)
    elif(m==4):
        print("The addition is: ",((a+b)+c)+d)
    else:
        print("Error")
elif(n==5):
    a=int(input("Enter 1 number:"))
    b=int(input("Enter 2 number:"))
    c=int(input("Enter 3 number:"))
    d=int(input("Enter 4 number:"))
    e=int(input("Enter 5 number:"))
    if(m==1):
        print("The multiplication is: ",(((a*b)*c)*d)*e)
    elif(m==2):
        print("The division is: ",(((a/b)/c)/d)*e)
    elif(m==3):
        print("The subtraction is: ",(((a-b)-c)-d)-e)
    elif(m==4):
        print("The addition is: ",(((a+b)+c)+d)+e)
    else:
        print("Error")
elif(n==6):
    a=int(input("Enter 1 number:"))
    b=int(input("Enter 2 number:"))
    c=int(input("Enter 3 number:"))
    d=int(input("Enter 4 number:"))
    e=int(input("Enter 5 number:"))
    f=int(input("Enter 6 number:"))
    if(m==1):
        print("The multiplication is: ",((((a*b)*c)*d)*e)*f)
    elif(m==2):
        print("The division is: ",((((a/b)/c)/d)/e)/f)
    elif(m==3):
        print("The subtraction is: ",((((a-b)-c)-d)-e)-f)
    elif(m==4):
        print("The addition is: ",((((a+b)+c)+d)+e)+f)
    else:
        print("Error")
elif(n==7):
    a=int(input("Enter 1 number:"))
    b=int(input("Enter 2 number:"))
    c=int(input("Enter 3 number:"))
    d=int(input("Enter 4 number:"))
    e=int(input("Enter 5 number:"))
    f=int(input("Enter 6 number:"))
    g=int(input("Enter 7 number:"))
    if(m==1):
        print("The multiplication is: ",(((((a*b)*c)*d)*e)*f)*g)
    elif(m==2):
        print("The division is: ",(((((a/b)/c)/d)/e)/f)/g)
    elif(m==3):
        print("The subtraction is: ",(((((a-b)-c)-d)-e)-f)-g)
    elif(m==4):
        print("The addition is: ",(((((a+b)+c)+d)+e)+f)+g)
    else:
        print("Error")
elif(n==8):
    a=int(input("Enter 1 number:"))
    b=int(input("Enter 2 number:"))
    c=int(input("Enter 3 number:"))
    d=int(input("Enter 4 number:"))
    e=int(input("Enter 5 number:"))
    f=int(input("Enter 6 number:"))
    g=int(input("Enter 7 number:"))
    h=int(input("Enter 8 number:"))
    if(m==1):
        print("The multiplication is: ",((((((a*b)*c)*d)*e)*f)*h)*g)
    elif(m==2):
        print("The division is: ",((((((a/b)/c)/d)/e)/f)/g)/h)
    elif(m==3):
        print("The subtraction is: ",((((((a-b)-c)-d)-e)-f)-g)-h)
    elif(m==4):
        print("The addition is: ",((((((a+b)+c)+d)+e)+f)+g)+h)
    else:
        print("Error")
elif(n==9):
    a=int(input("Enter 1 number:"))
    b=int(input("Enter 2 number:"))
    c=int(input("Enter 3 number:"))
    d=int(input("Enter 4 number:"))
    e=int(input("Enter 5 number:"))
    f=int(input("Enter 6 number:"))
    g=int(input("Enter 7 number:"))
    h=int(input("Enter 8 number:"))
    i=int(input("Enter 9 number:"))
    if(m==1):
        print("The multiplication is: ",(((((((a*b)*c)*d)*e)*f)*g)*h)*i)
    elif(m==2):
        print("The division is: ",(((((((a/b)/c)/d)/e)/f)/g)/h)/i)
    elif(m==3):
        print("The subtraction is: ",(((((((a-b)-c)-d)-e)-f)-g)-h)-i)
    elif(m==4):
        print("The addition is: ",(((((((a+b)+c)+d)+e)+f)+g)+h)+i)
    else:
        print("Error")
else:
    print("Some input error has been caused")
