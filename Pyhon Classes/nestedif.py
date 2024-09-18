name=str(input('Enter the students name:'))
JAMBscore=int(input('enter your JAMBscore:'))
if(JAMBscore>=140):
    print('You passed your JAMB')
    postutmescore=int(input('enter your postutmescore:'))
    if(postutmescore>=100):
       print('congrats you have been admitted')
    else:
       print('sorry you have failed,try again next year')
else:
    print('sorry you failed come back next year')
