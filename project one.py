print('welcome to the Coin GuessingGame !')
print('choose a method to toss the coin:')
print('1.using random.random()')
print('2.using random.randint()')
s = input('Enter your choice (1 or 2) \n')
import random
if s == '1' :
    random_number = random.random()
    if random_number >= 0.5:
        com_result = 'Heads'
    else:
        com_result = ' Tails'
elif s == '2':
    random_rad = random.randint(0,1)
    if random_rad == 0:
        com_result = "Heads"
    else:
        com_result = "tails"
       
else:
    print('Try again')
heads_tails_choice = input('Enter your Guess (Heads or Tails) \n').lower()
if heads_tails_choice == com_result.lower():
    print('Congeratualtion ! you win!')
else :
    print('Sorry! Please try again')

