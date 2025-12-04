from datetime import datetime
inpoot = open("input.txt").read()
#inpoot = open("eg.txt").read()

startTime = datetime.now()
inpoot = inpoot.split("\n")

## pad grid to 
toppad = ((len(inpoot[0])+2)*" ")
botpad = ((len(inpoot[0])+2)*" ")
inputpadded = []
inputpadded.append(toppad)

for line in inpoot:
    line = " "+line+" "
    inputpadded.append(line)

inputpadded.append(botpad)


#for line in inputpadded: print(line)




def eightwaysearch(y,x,find,map):
    result=0
    if map[y][x+1] == find: result+=1
    if map[y][x-1] == find: result+=1
    if map[y-1][x] == find: result+=1
    if map[y+1][x] == find: result+=1
    if map[y-1][x-1] == find: result+=1
    if map[y-1][x+1] == find: result+=1
    if map[y+1][x-1] == find: result+=1
    if map[y+1][x+1] == find: result+=1
    return(result)

find = "@"

goodrolls = 0

y=0
for line in inputpadded:
    x=0
    #if line[1] != " ":
    for char in line:
        if char == "@":
            if eightwaysearch(y,x,find,inputpadded) < 4:
                goodrolls += 1
        x+=1    
    y+=1

print(goodrolls)

print(datetime.now() - startTime)


##### if I'm at [5],[5] I need to check
# [5,6] right       [y][x+1]  
# [5,4] left        [y][x-1]
# [4,5] up          [y-1][x]
# [6,5] down        [y+1][x]
# [4,4] up left     [y-1][x-1]
# [4,6] up right    [y-1][x+1]
# [6,4] down left   [y+1][x-1]
# [6,6] down right  [y+1][x+1]

