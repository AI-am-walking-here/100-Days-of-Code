total = float(input('What was the total bill?\n'))
Tip = float(input('What percentage of tip would you like to give?\n')) * 0.01
people = float(input('How many ways is the bill split?\n'))


total = (total * Tip) + total
total /= people
total = round(total, 2)


print('Welcome to the Tip ,Calculator')
print(f'Everyone should pay {total}')