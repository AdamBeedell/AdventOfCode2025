from datetime import datetime

inpoot = open("input.txt").read()
#inpoot = open("eg.txt").read()

startTime = datetime.now()
ranges, ids = inpoot.split("\n\n")

ranges = ranges.split("\n")
ids = ids.split("\n")

goodids = set()        # <-- used to be dict
for r in ranges:
    s, f = r.split("-")
    for i in range(int(s), int(f) + 1):
        goodids.add(i)   # <-- instead of dict[i] = "fresh"

result = 0
freshstuff = [1]
freshstuff = set(freshstuff)

for id in ids[:10]:
    #print(id)
    num = int(id)
    #print(num)
    if num in goodids:    # <-- membership instead of dict.get(...)
        result += 1
        freshstuff.add(num)
        #print("adding")
   # else:
        #print("not adding")


#print(freshstuff)
print(result)

print(datetime.now() - startTime)