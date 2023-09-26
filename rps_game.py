import random
l=["rock", "Scissor", "paper"]
'''
rock-vs-paper->paper wins
rock-vs-scissor->rock wins
paper-vs-scissor->scissor wins

'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start......
1 Yes
2 No | Exit
'''))
    
    if uc == 1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Scissor
3 Paper            
'''))
            if userInput == 1:
                uchoice="rock"
            elif userInput == 2:
                uchoice="scissor"
            elif userInput == 3:
                uchoice="paper"
            else:
                print("Please enter valid input.")
            Cchoice = random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Game Draw")
                ucount = ucount+1
                ccount = ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=='scissor' and Cchoice=="paper"):
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Game User Win")
                ucount = ucount+1
            else:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Game Computer Win")
                ccount = ccount+1
        if ccount == ucount:
            print("Final Game Draw...")
            print("Computer Score", ccount)
            print("User Value", ucount)
        elif ccount > ucount:
            print("Final Computer Win the Game...")
            print("Computer Score", ccount)
            print("User Value", ucount)
        else:
            print("Final User win the Game...")
            print("Computer Score", ccount)
            print("User Value", ucount)
                
    else:
        break