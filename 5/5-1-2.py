from datetime import datetime

inpoot = open("input.txt").read()
#inpoot = open("eg.txt").read()

startTime = datetime.now()
ranges, ids = inpoot.split("\n\n")

ranges = ranges.split("\n")
ids = ids.split("\n")


result = 0
freshstuff = []

for id in ids:
    #print(id)
    id = int(id)
    #print(num)
    stop = 0
    while stop == 0:
        for r in ranges:
            s, f = r.split('-')
            if id in range(int(s),int(f)):   
                result += 1
                freshstuff.append(id)
                stop = 1
        stop = 1
            

print(freshstuff)
print(result)

print(datetime.now() - startTime)