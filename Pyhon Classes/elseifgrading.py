score=int(input('enter your score:'))
if(score>=70 and score<=100):
    print('A')
elif(score>=60 and score<=69):
    print('B')
elif(score>=50 and score<=59):
    print('C')
elif(score>=40 and score<=49):
    print('D')
elif(score>=0 and score<=39):
    print('F')
else:
    print('invalid input')