#inpoot = open("input.txt").read()
inpoot = open("eg.txt").read()

#from datetime import datetime
#startTime = datetime.now()

inpoot = inpoot.split("\n")


###  Parse the input by line by brackets

import re

regex = "\[(.*?)\] (\(.*\)) {(.*)}"
switchpuzzles = []
for line in inpoot:
    a,b,c = re.search(regex, line).groups()
    switchpuzzles.append({"a": a, "b": b, "c": c})








print(result)
#print(datetime.now() - startTime)