#write a programme to show the use of conditional operator(greater among 2 numbers)
def find_greater():
    num1=int(input("enter the first number: "))
    num2=int(input("enter the second nuumber: "))
    greater=num1 if num1>num2 else num2
    print('The greater number:',greater)
find_greater()

#wite a programme to check whether a given number is even or odd(by using conditional operator)
def check_even_odd():
    num=int(input("Enter a number: "))
    result="Even" if num%2==0 else "Odd"
    print("Number is: ",result)
check_even_odd()