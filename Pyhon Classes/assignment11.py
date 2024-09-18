#write a programme to convert temperature from degree celcius to fahrenheit and vice versa,with the formula:9c/5+32
celcius=float(input("enter temperature in celcius: "))
fahrenheit=(celcius*9/5) + 32
print('%.2f Celcius is : %0.2f Fahrenheit' %(celcius,fahrenheit)) 
fahrenheit=float(input("enter the temperature in fahrenheit: "))
celcius=(fahrenheit-32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celcius' %(fahrenheit,celcius))