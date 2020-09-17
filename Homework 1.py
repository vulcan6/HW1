#Name: Erick Jimenez
#PSID: Birthday Calculator
#Project: Birthday Calculator
print('Welcome to the Birthday Calculator')
print('Please input the current day:\n')

cm = int(input('Please type in the month:'))
cd = int(input('Please type in the day:'))
cy =  int(input('Please type in the year:'))

print('Please type in your birthday:')

bm = int(input('Month:'))
bd = int(input('Day:'))
by =  int(input('Year:'))

print('You are', cy-by, 'years old.')
if (cm,cd) == (bm,bd):
    print('Happy Birthday!')