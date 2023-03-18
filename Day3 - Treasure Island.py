print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to win the fight, with the big scarry owl bear.\n\n") 



print('''You are a brave warrior, currently fighting a terrifying 
beast with the boddy of a bear and the head of an owl.In order to 
get the treas you will need to fight off this owlbear\n\nThe owlbear swings!''')
choice1 = input('Will you dodge Left or Right? ').lower()

if choice1 == 'left':
    print('''You roll to the left, BEARly dogging the attacks. The owlbear charges at you, but you
notice a nearby pool will you stand your ground to the owl bear or jump away to the pool''')
    choice2 = input('swim or wait? ').lower()
    if choice2 == 'wait':
        print('The bear is scared, he lets you pass to the tresure/n which door do you choose?\n')
        choice3 = input('Red, Yellow, Blue? ').lower() 
        if choice3 == 'yellow':
            print('You found the golden tresure you win!')
        elif choice3 == 'blue':
            print('You found water you drown')
        else:
            print('you explode')
    else:print('You hit you head jumping in. You die game over!')
else:
    print('You dodge right and trip over a rock. You die game over!')