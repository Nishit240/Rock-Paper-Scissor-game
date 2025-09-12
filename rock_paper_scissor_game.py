import random
 
bot = random.choice([-1,0,1])
you1 = input("Enter Your Choice : ")
youstr = you1.lower()
youDict = {"p" : 1, "r" : -1 , "s" :0}
reverseDict = {1 : "Paper", -1 : "Rock" , 0 : "Scissor"}
you = youDict[youstr]
 
print(f"You chose {reverseDict[you]} Bot chose {reverseDict[bot]}")

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
if ((bot - you) == -1 or (bot - you)==2):
    print("You Lose..")
else:
    print("You Win!!")

elif((bot==0 and you==0) or (bot==-1 and you==-1) or (bot==1 and you==1)):
    print("Its a Tie.")

else:
    print("Enter correct Choice.")
'''

