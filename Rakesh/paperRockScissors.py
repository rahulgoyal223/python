# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:40:40 2018
problem statment 
======================================================
Make a two-player Rock-Paper-Scissors game. 

Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
======================================================
@author: Rakesh
"""

def PromptUser():
     ch= input("Press Y to play : ")
     if ch =='Y':
         return True
     else:
         return False
     
def UserWin(userChoice, systeChoice):
    print("\nYou Won !!\n" )
    print("My choice was : " + systeChoice)
    print("your choice was : "+ userChoice)
    return

def UserLost(userChoice, systeChoice):
    print("\nYou lost !!\n")
    print("My choice was : " + systeChoice)
    print("your choice was : "+ userChoice)
    return
     
        
import random
shallContinue = True
lstChoice = ['paper', 'scissors', 'rock']
while shallContinue:
    userChoice = input("Enter your choice : ")
    SystemChoice = lstChoice[random.randint(0,2)]
    # both choice are same
    if SystemChoice == userChoice:
        print("it's tie!!")
        print("we both choose : " + userChoice)
        shallContinue = PromptUser()
    elif userChoice == 'paper':
        if SystemChoice =='scissors':
            UserLost(userChoice,SystemChoice)
        else:
            UserWin(userChoice,SystemChoice)
        shallContinue = PromptUser()
    elif userChoice == 'scissors':
        if SystemChoice =='rock':
            UserLost(userChoice,SystemChoice)
        else:
            UserWin(userChoice,SystemChoice)
        shallContinue = PromptUser()
    elif userChoice == 'rock':
        if SystemChoice =='paper':
            UserLost(userChoice,SystemChoice)
        else:
            UserWin(userChoice,SystemChoice)
        shallContinue = PromptUser()
    
    
    

         
     