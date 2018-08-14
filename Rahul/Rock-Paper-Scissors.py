from random import choice
againPlay = True
s = ['Rock', 'Scissors', 'Paper']
while againPlay:
    userInput = input('''Enter a input from ['Rock', 'Scissors','Paper']:''')
    comp = choice(s)
    while userInput==comp:
        comp = choice(s)

    if userInput == 'Rock':
        if comp == 'Scissors':
            print("Computer's input is", comp, ": You win")
        elif comp == 'Paper':
            print("Computer's input is", comp, ": You lose")

    elif userInput == 'Scissors':
        if comp == 'Paper':
            print("Computer's input is", comp, ": You win")
        elif comp == 'Rock':
            print("Computer's input is", comp, ": You lose")

    elif userInput == 'Paper':
        if comp == 'Rock':
            print("Computer's input is", comp, ": You win")
        elif comp == 'Scissors':
            print("Computer's input is", comp, ": You lose")
    else:
        print("Invalid input")

    playAgain = input("Enter yes to re-play:")
    if playAgain == 'yes':
        againPlay = True
    else:
        againPlay = False
