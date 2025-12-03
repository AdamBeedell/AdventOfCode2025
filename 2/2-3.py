import math
from itertools import islice

# Don't shadow the builtin 'input'
with open("input.txt") as f:
    ranges = f.read().split(",")

resultsarray = []

def factorizer(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:
                factors.append(num // i)
    return factors


def atomicslash(text):
    text = str(text)
    textlen = len(text)
    factors = factorizer(textlen)
    listoflists = []

    # each factor is a potential chunk length
    for chunk_len in factors:
        # skip the trivial "no split" case
        if chunk_len == textlen:
            continue
        # (extra safety; factorizer should only give divisors anyway)
        if textlen % chunk_len != 0:
            continue

        num_chunks = textlen // chunk_len
        it = iter(text)
        listyy = [list(islice(it, chunk_len)) for _ in range(num_chunks)]
        listoflists.append(listyy)

    return listoflists


for therange in ranges:
    start, finish = therange.split("-")
    for i in range(int(start), int(finish) + 1):
        dust = atomicslash(i)
        for ashes in dust:
            # e.g. ['4','4','4'] -> "444"
            chunks = [''.join(chunk) for chunk in ashes]
            if len(set(chunks)) == 1:
                print(set(chunks), "from", i)
                resultsarray.append(i)   # full number is the target

resultsset = set(resultsarray)
results = sum(resultsset)

print("Final Result:")
print(results)