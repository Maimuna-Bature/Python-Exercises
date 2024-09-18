#write a programme to calculate factorial using for loop
def factorial_for(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

#write a programme to calculate factorial using while loop
def factorial_while(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact
num = int(input("Enter a number: "))
print("Factorial using for loop:", factorial_for(num))
print("Factorial using while loop:", factorial_while(num))