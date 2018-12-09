import random

"""
1 - Rock / Камінь
2 - Scissors / Ножниці
3 - Paper / Папір
"""

x = random.randint(1, 3)
print('Enter the action number where: \n 1 - Rock \n 2 - Scissors \n 3 - Paper ')
y = input()

#lose
if x == 1 and y == "2":
    print("Scissors vs Rock! You lose!")
elif x == 2 and y == "3":
    print("Paper vs Scissors! You lose!")
elif x == 3 and y == "1":
    print("Rock vs Paper! You lose!")

#won
elif x == 2 and y == "1":
    print("Rock vs Scissors! You won!")
elif x == 3 and y == "2":
    print("Scissors vs Paper! You won!")
elif x == 1 and y == "3":
    print("Paper vs Rock! You won!")

#draw
elif x == 1 and y == "1":
    print("Rock vs Rock! Draw!")
elif x == 2 and y == "2":
    print("Scissors vs Scissors! Draw!")
elif x == 3 and y == "3":
    print("Paper vs Paper! Draw!")

else:
    print("What?")