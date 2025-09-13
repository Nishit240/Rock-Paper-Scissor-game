import random

choices = {"r": -1, "p": 1, "s": 0}
reverse_choices = {-1: "Rock", 1: "Paper", 0: "Scissor"}

score_you = 0
score_bot = 0

while True:
    you1 = input("Enter for Rock = r, Paper = p or Scissor = s: ").lower()
    if you1 not in choices:
        print("Invalid choice, try again!\n")
        continue
    
    you = choices[you1]
    bot = random.choice(list(choices.values()))
    
    print(f"You chose {reverse_choices[you]} | Bot chose {reverse_choices[bot]}")

    if you == bot:
        print("It's a Tie!")
    elif (you - bot) % 3 == 1:
        print("🎉 You Win!")
        score_you += 1
    else:
        print("😢 You Lose..")
        score_bot += 1

    print(f"Score -> You: {score_you} | Bot: {score_bot}\n")

    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in ["y" ,"n" ,"no" ,"yes"]:

            break
        else:
            print("❌ Invalid input! Please type 'y' or 'n'.")

    if (play_again == "n" or  play_again == "no"):
        print("Final Score:", f"You {score_you} - {score_bot} Bot")
        print("Thanks for playing! 👋")
        break

'''
if (bot==-1 and you==1 ):
    print("YOU WIN!!")

elif (bot==-1 and you==0 ):
    print("YOU Lose..")

elif (bot==1 and you==0 ):
    print("YOU WIN!!")

elif (bot==1 and you==-1 ):
    print("YOU Lose..")

elif (bot==0 and you==1 ):
    print("YOU Lose!!")

elif (bot==0 and you==-1 ):
    print("YOU WIN!!")

elif((bot==0 and you==0) or (bot==-1 and you==-1) or (bot==1 and you==1)):
    print("Its a Tie.")

else:
    print("Enter correct Choice.")
'''

'''
if ((bot - you) == -1 or (bot - you)==2):
    print("You Lose..")
else:
    print("You Win!!")

elif((bot==0 and you==0) or (bot==-1 and you==-1) or (bot==1 and you==1)):
    print("Its a Tie.")

else:
    print("Enter correct Choice.")
'''

