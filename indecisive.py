## Project start 10/16/2022

from datetime import date                        ##Variable to show time
today = date.today()                             
d2 = today.strftime("%B %d, %Y")

name = input('What is your name?\n')
print('Nice to meet you,', name+'!\n' 'Todays date is', d2)         ##Gather users name for greeting

foodtype = input('What kind of food are we feeling today?\n')
while foodtype.lower() == 'idk':
    print('Be a little more specific, I cant help if youre not!')
    break 
foodtype = input('What kind of food are we feeling today?\n')

print('Okay, you want', foodtype, 'lets see what we can do.')

wantsfridge = input('Do you want to cook from home?\n')         ##Does user want to cook from home
while wantsfridge.lower() != 'yes':
    if wantsfridge.lower() == 'no':
        print('Okay, moving on.')
    else:
        print('That is not valid input. Please type "Yes" or "No".')
    break

## Implement API call for store hours that have food near user

while wantsfridge == 'yes':
    fridgecontent = input('Do you have stuff that could make', foodtype ,'in your fridge?')     ##Evaluating if user has food in fridge to make dinner
    while fridgecontent.lower() != 'yes':
        if fridgecontent.lower() == 'no':
            foodorder = input('Could you go and buy what you need?\n')
            while foodorder.lower() != 'no':
                groceries = input('What do you need? Type it here, seperating your items with commas.')
                print(f'Great! Lets make sure we get {groceries} so we can get to cooking.')

eatout = input('You dont want to cook from home, what do you want?')
print(f'Great! {eatout} sounds great! Lets go get it.')

##Implement API call related to food service name ^^^
