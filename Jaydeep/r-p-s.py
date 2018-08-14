#two-player Rock-Paper-Scissors game.

inputA = input("Player 1's play : ").strip()
inputB = input("Player 2's play : ").strip()
allowed = ['r','p','s']
if inputA not in allowed or inputB not in allowed:
    raise SystemExit("invalid input")
if inputA == inputB:
    raise SystemExit("tie")

winner = 'B'
if(inputA == 'r'):
    if(inputB == 's'):
        winner = 'A'
elif(inputA == 'p'):
    if(inputB == 'r'):
        winner = 'A'
else:
    if(inputB == 'p'):
            winner = 'A'

print ("winner is " + winner)
