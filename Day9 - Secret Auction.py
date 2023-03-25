logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

from replit import clear
bid_continue = True
print(logo)
bidictionary = {}

while bid_continue:
    print('Welcome to the secret auction')
    name = input('What is your name? ')
    bid = int(input('What is your bid amount? '))
    bidictionary[name] = bid
    other_bidders = input('Are there other bidders? "t" or "f" ')

    if other_bidders == "f":
        bid_continue = False
        clear()
    else:
        clear()

highest_bid = 0
highest_bidder = ''

for bidder, bid_amount in bidictionary.items():
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = bidder


print(f'The highest bidder is {highest_bidder} with a bid of {highest_bid}')

#dictionary with info
#are there any other bidders?
#compare scores and find winner