inputseq=[int(x) for x in input().split()]
if len(inputseq)!=2:
    raise SystemExit("invalid input")
arr=[int(x) for x in input().split()]
if len(arr)!=inputseq[0]:
    raise SystemExit("invalid input")
setA={int(x) for x in input().split()}
if len(setA)!=inputseq[1]:
    raise SystemExit("invalid input")
setB={int(x) for x in input().split()}
if len(setB)!=inputseq[1]:
    raise SystemExit("invalid input")
happiness=0
for i in arr:
    if i in setA:
        happiness+=1
    elif i in setB:
        happiness-=1

print(happiness)