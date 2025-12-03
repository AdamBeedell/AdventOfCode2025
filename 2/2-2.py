inpoot = open("input.txt").read()
#inpoot = open("eg.txt").read()
inpoot = inpoot.split(",")

import math
from itertools import islice

result = 0

def atomicslash(text): 
    text=str(text)
    numba = int(text)
    textlen = len(text)
    listy = factorizer(textlen)
    pairs = pair(listy)
    listoflists = []
    for lil, big in pairs:
        it = iter(text)
        listyy = [list(islice(it, lil)) for _ in range(big)] 
        listoflists.append(listyy)
    return(listoflists)


def pair(listy):
    n = 2
    it = iter(listy)
    pairs = [list(islice(it, n)) for _ in range((len(listy) + n - 1) // n)] ## copied this one liner but didnt ask chatgpt and edited and typed it all by my self
    return(pairs) 


def factorizer(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            big = num // i
            factors.append(i)
            factors.append(big)
    return factors

for therange in inpoot:
    start,finish = therange.split("-")
    for i in range(int(start),int(finish)+1):
        #print(i)
        dust = atomicslash(i)
        for ashes in dust:
            chunks = [''.join(chunk) for chunk in ashes]  # e.g. [['1','2','3'], ...] -> ['123', '123', ...]
            if len(set(chunks)) == 1:
                print(set(chunks), "from", i)
                result += i   # full number is the target

print("Final Result:")
print(result)

