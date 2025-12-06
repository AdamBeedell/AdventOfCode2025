from datetime import datetime

inpoot = open("input.txt").read()
#inpoot = open("eg.txt").read()

startTime = datetime.now()
ranges, ids = inpoot.split("\n\n")

ranges = ranges.split("\n")
ids = ids.split("\n")

goodidsdict = {}

for r in ranges:
    s,f = r.split("-")
    for i in range(int(s),int(f)+1):
        goodidsdict[i] = "fresh"


result = 0
freshstuff = {}

for id in ids:
    if goodidsdict.get(int(id)) == "fresh":
        result += 1
        freshstuff[id] = "fresh"


print(freshstuff)
print(result)


print(datetime.now() - startTime)