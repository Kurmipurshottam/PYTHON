try:
    num1=int(input("enter number 1 = "))
    num2=int(input("enter number 2 = "))
    ans=num1/num2
    print("ans = ",ans)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("can not divided by zero")
