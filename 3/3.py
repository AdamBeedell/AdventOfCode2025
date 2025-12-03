inpoot = open("input.txt").read()
#inpoot = open("eg.txt").read()
inpoot = inpoot.split("/n")




for line in inpoot:
    pointerA=0
    pointerB=0
    line = str(line)
    for char in line:
        if char > pointerA:
            pointerA = char
        elif char > pointerB:
            pointerB = char
    print(pointerA, pointerB)
