while True:
    input("Hello")
    input("WELCOME TO PYTHON CALCULATOR")
    input("ENTER YOUR PROBLEM")
    a=float(input("enter first number:"))
    b=float(input("enter second number:"))
    input("choose the operator + - * / % //")
    n=input("enter the operator")

    if n== "+":
        print(a+b)
    elif n== "-":
        print(a-b)
    elif n== "*":
        print(a*b)
    elif n== "/":
        print(a/b)
    elif n== "%":
        print(a%b)
    elif n== "//":
        print(a//b)
    else:
        print(null)
    c=int(input("To continue press 1 or To exit press 0"))
    if c== 1:
        continue;
    elif c== 0:
        break;
