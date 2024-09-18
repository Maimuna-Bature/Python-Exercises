#write a programme to check if a year is a leap year
year=int(input('enter a year: '))
if year%4==0 and year%100!=0:
    print("it is a leap year")
elif year%400==0:
    print("it is a leap year")
else:
    print("it is not a leap year")
