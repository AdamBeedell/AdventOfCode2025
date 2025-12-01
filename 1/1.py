input = open("input.txt").read()
#input = open("eg.txt").read()
input = input.split("\n")

Dial = [0]*100
Dial[0] = 1

DialCurrent = 50

result = 0

## Change R to "", change L to -

def intify(instruction):
    if instruction[0] == "R":
        instruction = instruction.replace("R","")
    elif instruction[0] == "L":
        instruction = instruction.replace("L","-")
    return int(instruction)



def turn(notches):
    global DialCurrent
    DialCurrent = (DialCurrent + notches) % 100
    print(DialCurrent)
    return(Dial[DialCurrent])


for instruction in input:
    notches = intify(instruction)
    result += turn(notches)


print(result)