#Print the series 1,1 2, 1 2 3, 1 2 3 4, 1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Print the series 1 ,2 2 ,3 3 3 ,4 4 4 4 ,5 5 5 5 5
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

#Print the series 1 2 3 4 5 6 7 8 9 10
def print_triangle():
    num=1  
    for i in range(1, 5):
        for j in range(i):
            print(num, end=" ")
            num +=1
            if num > 10:
               break
        print()
print_triangle()

#print a series if nubers to form an equiliteral triangle
for i in range(1,6):
    print("  "*(5-i), end=" ")
    print(*range(1, i+1), *range(i-1, 0, -1))
        


