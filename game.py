# Write your code here
import random
playing = True

name = input('Enter your name: ')
print('Hello, {}'.format(name))
ratings = open('rating.txt', 'r')
score = 0

for rating in ratings:
    re_name, re_score = rating.split()
    if re_name == name:
        score = int(re_score)

options = input()

if len(options) == 0:
    options = "rock,paper,scissors"

option_lst = options.split(",")
sides = len(option_lst) // 2

print("Okay, let's start")

while playing:
    user_pick = input()
    comp_pick = random.choice(option_lst)
    
    if user_pick == '!exit':
        print("Bye!")
        break
    
    if user_pick == '!rating':
        print("Your rating: {}".format(score))
        continue
    
    higher = []
    lower = []
    
    if user_pick in option_lst:
        idx = option_lst.index(user_pick)

        for pos in range(0, sides * 2):
            if pos < sides:
                lower.append(option_lst[idx - 1 - pos])
            else:
                higher.append(option_lst[idx - 1 - pos])
    
    if user_pick == comp_pick:
        outcome = 'draw'
    elif comp_pick in higher:
        outcome = 'lose'
    elif comp_pick in lower:
        outcome = 'win'
    else:
        outcome = 'invalid'

    if outcome == 'draw':
        score += 50
        print(f"There is a draw {comp_pick}")
    elif outcome == 'lose':
        print(f"Sorry, but computer chose {comp_pick}")
    elif outcome == 'win':
        score += 100
        print(f"Well done. Computer chose {comp_pick} and failed")
    else:
        print("Invalid input")
