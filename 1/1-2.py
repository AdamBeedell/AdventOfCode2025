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

### newbit
## intially was going to do some ifs, then saw the turns go to like 800
## there's a clever modulo for this but cba, just break it into 1s and it should work
def bigturn(notches):
    global DialCurrent
    if notches < 0:
        for i in range(abs(notches)):
            turn(-1)
    elif notches > 0:
        for i in range(abs(notches)):
            turn(1)
    return 

def turn(notches):
    global DialCurrent
    global result
    DialCurrent = (DialCurrent + notches) % 100
    #print(DialCurrent)
    result += Dial[DialCurrent]
    return


for instruction in input:
    notches = intify(instruction)
    bigturn(notches)


print(result)
