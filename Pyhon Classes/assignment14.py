#write a programme to accept the height of a person in centimeter and categorize the person according to their height 
height=float(input('enter your height:'))
if(height<=150):
    print('You are Short!')
elif(height>=151 and height<=164):
    print('You are Average!')
elif(height>=165 and height<=189):
    print('You are Tall!')
else:
    print('You are Very Tall!')
