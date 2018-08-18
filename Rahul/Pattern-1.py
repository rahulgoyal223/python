#inputSeq=int(input("Enter a number in from 1-9:"))

#if inputSeq<1 or inputSeq>9 :
 #   raise SystemExit("invalid input. Enter a number in from 1-9")

for i in range(1,9):
    print(int(i*(10**(i-1)+10**(i-2)+10**(i-3)+10**(i-4)+10**(i-5)+10**(i-6)+10**(i-7)+10**(i-8)+10**(i-9))))