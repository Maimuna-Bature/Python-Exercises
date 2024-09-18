#write a programme to swap 2 numbers without using a third varible
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print("Before swapping")
print("Number1: ",num1)
print("Number2: ",num2)
num1,num2=num2,num1
print("After swapping")
print("Number1: ",num1)
print("Number2: ",num2)