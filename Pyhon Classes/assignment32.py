#Squares of 1st 10 natural numbers and their sum
total = 0
for i in range(1, 11):
    square = i ** 2
    total += square
    print(f"{i}^2 = {square}")
print("Sum of squares:", total)

#Check if a number is Palindrome
num = int(input("Enter a number: "))
if num == int(str(num)[::-1]):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
