import math
found = False
for c in range(0, 1000):
    if found:
        break
    for b in range(0, c):
        if found:
            break
        for a in range(0, b):
            if math.sqrt(math.pow(a, 2) + math.pow(b, 2)) == c and a + b + c == 1000:
                found = True
                print(a)
                print(b)
                print(c)
                print(a*b*c)
                break
print("Done")