#Product and average of 1st N natural numbers
n = int(input("Enter a number: "))
product = 1
addition= 0
for i in range(1, n + 1):
    product *= i
    addition += i
average = addition / n
print("Product:", product)
print("Average:", average)