rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#random num gen
import random              

choice = (input("Rock, Paper, or scissors ").lower())
print(choice)
if choice == 'rock':
    print(rock)
    choice =1
elif choice == 'paper':
    print(paper)
    choice =2
else:
    print(scissors)
    choice =3

print('Your oppenent chooses...')

op_choice = random.randint(1,3)

if op_choice == 1:
    print(rock)
elif op_choice == 2:
    print(paper)
else:
    print(scissors)
    op_choice = 3

if choice == op_choice:
    print("IT's A TIE!!!")
elif choice == 1:
    if choice - op_choice == -2:
        print("YOU WIN!!!")
    else:
        print("YOU LOSE!!!")
elif choice == 2:
    if choice - op_choice == 1:
        print("YOU WIN!!!")
    else:
        print("YOU LOSE!!!")
else:
    if choice - op_choice == 1:
        print("YOU WIN!!!!")
    else:
        print("YOU LOSE!!!")




