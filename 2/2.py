input = open("input.txt").read()
#input = open("eg.txt").read()
input = input.split(",")

result = 0

def stringbiscect(text):
    text=str(text)
    x, y = text[:len(text)//2 + len(text)%2], text[len(text)//2 + len(text)%2:]
    return(x, y)

#stringbiscect("123456789")

for therange in input:
    start,finish = therange.split("-")
    for i in range(int(start),int(finish)+1):
        #print(i)
        x,y = stringbiscect(i)
        if x == y:
            print(i)
            result += i

print("Final Result:")
print(result)