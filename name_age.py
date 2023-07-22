## Program to prompt for Name, Age and Calc Birth Yr
## Created by Zen K. Silva
## Created on:  11/4/2021
## lAST modified on: 06|16|2023
def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    if line == 1:
        name = input('What is your name? ')
        myresponse = input('You entered ' + name + '.  is this correct? (Y, N) ')
        if myresponse == 'y':
            goto(2)
        elif myresponse == 'Y':
            goto(2)
        elif myresponse == 'yes':
            goto(2)
        elif myresponse == 'Yes':
            goto(2)
        else:
            goto(1)
    elif line == 2:
        age = input('How old are you? ')
        myresponse = input('You entered ' + age + ' is this correct (Y, N)? ')
        if myresponse == 'y':
            goto(3)
        elif myresponse == 'Y':
            goto(3)
        elif myresponse == 'yes':
            goto(3)
        elif myresponse == 'Yes':
            goto(3)
        else:
            goto(2)
    elif line == 3:
        currentyr = 2023
        birthyear = currentyr - int(age)
        print('Hello ' + name + '!  You were born in ' + str(birthyear) + '.')
        break