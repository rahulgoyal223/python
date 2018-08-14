#Write a Python program to count the number of characters (character frequency) in a string.

inputstring = input("enter values : ").strip()
uniquelist =list(set(list(inputstring)))
uniqueCounts = dict()
for ch in inputstring:
    if ch in uniqueCounts:
        uniqueCounts[ch] += 1
    else:
        uniqueCounts[ch] = 1
print (uniqueCounts)
