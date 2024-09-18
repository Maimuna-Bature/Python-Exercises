try:
    a=int(input("enter a number: "))
    b=int(input("enter a second number: "))
    num=a/b
    print(num)
except ZeroDivisionError:
    print("The progrmmed crash but I continued")
else:
    print("the result is:",num)
#second example with multple excepts
try:
    x=int(input('enter a number: '))
    y=1/x
except ValueError:
    print('invalid input! please enter a number.')
except ZeroDivisionError:
    print('cannot divide by zero')
except Exception:
    print("an unexpected error occured")
else:
    print("the result is:",y)