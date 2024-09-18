#write a programme that accepts 2 numbers from the user and perform 5 basic arithmetic operations on it
try:
    num1=int(input('enter the first number: '))
    num2=int(input('enter the second number: '))
    addition=num1+num2
    subtraction=num1-num2
    multiplication=num1*num2
    division=num1/num2
    modulus=num1%num2
    print('Addition is:',addition)
    print('Subtraction is:',subtraction)
    print('Multiplication is:',multiplication)
    print('Division is:',division)
except ZeroDivisionError:
    print('cannot divide by zero')
else:
    print('Modulus is:',modulus)