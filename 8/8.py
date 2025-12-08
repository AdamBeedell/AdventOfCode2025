#inpoot = open("input.txt").read()
inpoot = open("eg.txt").read()

#from datetime import datetime
#startTime = datetime.now()

inpoot = inpoot.split("\n")

junctionboxes = []

for row in inpoot:
    junctionboxes.append(row.split(","))

## Gotta connect up points by nearest neighbor
## mesh/graph structures are OK doesnt need to be a line
## Connecting a-b-c-d-e-a is a possible and valid step

def doPythag(a,b,c,x,y,z): # maybe 2 throuples
    ### abc cooord to xyz coord distance
    distance = 1
    return(distance)

def connect(?):
    ### no idea how this'll work yet
    return("??")
           

for box in junctionboxes:
    tempresults = [] ### dict?? Dont want dedupes without it counting a step
    for otherbox in junctionboxes:
        distance = doPythag(box[0], box[1], box[2], otherbox[0], otherbox[1], otherbox[2]) ## probably condense this to b1 b2 for brevity
        line = {
            "connection": b1-b2, ## this dont work 
            "distance": distance
            }
        tempresults.append(line)
    tempresults.sort ## check syntax
    connect(?)


print(result)
#print(datetime.now() - startTime)