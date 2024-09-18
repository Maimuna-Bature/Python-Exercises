#write a programme to print the largest of 3 numbers
def find_largest():
    num1=int(input("enter the first number: "))
    num2=int(input("enter the second number: "))
    num3=int(input("enter the third number: "))
    if num1==num2==num3:
        print("the numbers are the same")
    elif num1==num2 or num1==num3 or num2==num3:
        print("two numbers are the same")
    else:
      if num1>=num2 and num1>=num3:
         largest=num1
      elif num2>=num1 and num2>=num3:
         largest=num2
      else:
          num3>=num1 and num3>=num1
          largest=num3
    print("the largest number is: ",largest)
find_largest()