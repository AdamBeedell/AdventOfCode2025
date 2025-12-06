#inpoot = open("input.txt").read()
inpoot = open("eg.txt").read()


## Prep data - Decided against figuring out how to split into columns, rows then addressable blocks gets there
rows = inpoot.split("\n")
maths = []

for row in rows:
    chars = row.split() ##### This splits on a greedy amount of whitespace, must be removed
    maths.append(chars)


### eg.txt and input.txt have different heights, this is hardcoded in here and requires a change, it'd be able to both just looping instead but I'm just trying to quickly get to 6-2
#def DoOp(i):
#    global maths
#    if maths[-1][i] == "*":
#        answer = int(maths[0][i])*int(maths[1][i])*int(maths[2][i])*int(maths[3][i])
#    if maths[-1][i] == "+":
#        answer = int(maths[0][i])+int(maths[1][i])+int(maths[2][i])+int(maths[3][i])
#    return(answer)



result = 0
for i in range(0,len(maths[0])):
    result += DoOp(i)

print(result)