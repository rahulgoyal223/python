from random import choice
againPlay = True
s = ['Rock', 'Scissors', 'Paper']
while againPlay:
    userInput = input('''Enter a input from ['Rock', 'Scissors','Paper']:''')
    if userInput not in s:
        raise SystemExit("invalid input")
    loser = 'You'
    comp = choice(s)
    while userInput==comp:
        comp = choice(s)
    if userInput == 'Rock':
        if comp == 'Scissors':
            loser = 'computer'

    elif userInput == 'Scissors':
        if comp == 'Paper':
            loser = 'computer'

    elif userInput == 'Paper':
        if comp == 'Rock':
            loser = 'computer'

    if loser=='computer':
        print("Computer's input is", comp, ": You win")
    else:
        print("Computer's input is", comp, ": You Lose")


    playAgain = input("Enter yes to re-play:")
    if playAgain == 'yes':
        againPlay = True
    else:
        againPlay = False
