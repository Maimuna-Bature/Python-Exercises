#write a programme to print the Series 1: 10, 9, 8, ..., 1
print("Series 1:")
for i in range(10, 0, -1):
    print(i, end=", ")

#write a programme to print the Series 2: 2, 4, 6, 8, ..., 20
print("\nSeries 2:")
for i in range(2, 22, 2):
    print(i, end=", ")

#write a programme to print the Series 3: 10, 13.5, 17, 20.5, ...
print("\nSeries 3:")
num = 10
while num <= 20.5:
    print(num, end=", ")
    num += 3.5
