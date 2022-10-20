from datetime import date                        ##Variable to show time
today = date.today()
d2 = today.strftime("%B %d, %Y")

name = input('What is your name?\n')
print('Nice to meet you,', name+'!\n' 'Todays date is', d2)         ##Gather users name for greeting


foodtype = input('What kind of food are we feeling today?\n')
while foodtype.lower() == 'idk':
    print('Be a little more specific, I cant help if youre not!')
    foodtype = input('What kind of food are we feeling today?\n')


print('Okay, you want', foodtype, 'lets see what we can do.')

wantsfridge = 'x'
while wantsfridge.lower() != 'yes':
    wantsfridge = input('Do you want to cook from home?\n') ##Does user want to cook from home
    if wantsfridge.lower() == 'no':
        print('Okay, moving on.')
        break
    elif wantsfridge.lower() == 'yes':
        break
    else:
        print('That is not valid input. Please type "Yes" or "No".')

## Implement API call for store hours that have food near user

fridgecontent = 'x'
while wantsfridge == 'yes':
    while fridgecontent.lower() != 'yes':
        fridgecontent = input(f'Do you have stuff that could make {foodtype} in your fridge?\n')      ##Evaluating if user has food in fridge to make dinner
        if fridgecontent.lower() == 'no':
            foodorder = input('Could you go and buy what you need?\n')
            while foodorder.lower() != 'no':
                groceries = input('What do you need? Type it here, seperating your items with commas.')
                print(f'Great! Lets make sure we get {groceries} so we can get to cooking.')

eatout = input('You dont want to cook from home, what do you want?\n')
print(f'Great! {eatout} sounds great! Lets go get it.')
