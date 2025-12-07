inpoot = open("input.txt").read()
#inpoot = open("eg.txt").read()

from datetime import datetime
startTime = datetime.now()

## Aim here is to inport a map, then once imported to start at the S (only one so far)
## draw a line down till you hit a ^
## Make a new line to either side
## Continue those lines down as before
## Count the splits

## Prep data
rows = inpoot.split("\n")

themap = []
for row in rows:
    themap.append(list(row)) ### make cells replaceable


### Find Start

def findS():
    global themap
    for i in range(0,len(themap[0])):
        if themap[0][i] == "S":
            coord = (0,i) ## oh hey tuples
            return (coord)

result = 0
start = findS()
themap[start[0]][start[1]] = "|" ### less checks later

### maybe just treat this as transformations

def transform(y,x):
    global themap
    global result
    if themap[y-1][x] == "|" and themap[y][x] == "^":
        themap[y][x-1] = "|"
        themap[y][x+1] = "|"
        #print(f"did a beamsplit around {y},{x}, added 2")
        result += 1
    elif themap[y-1][x] == "|":
        themap[y][x] = "|"
        #print(f"drew beam down around {y},{x}")
        

y=1 # skip first row dodge out-of-bounds errors
for row in themap[1:]: # skip first row dodge out-of-bounds errors
    x=0
    for char in row:
        transform(y,x)
        x+=1
    y+=1

print(result)
### there's no instances in the puzzle of 2 beam splitters next to each other. 
# This means no rule needed ****CURRENTLY**** for how to handle a beam splitter attempting to transform another beamsplitter
print(datetime.now() - startTime)