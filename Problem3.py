import math


def is_prime(l):
    for x in range(2, int(math.ceil(math.sqrt(l)))):
        if l % x == 0:
            return False
    return True

n = 600851475143

prime = 0
print('Starting Value: ' + str(int(math.ceil(math.sqrt(n)))))
for x in range(int(math.ceil(math.sqrt(n))), 0, -1):
    if is_prime(x) and n % x == 0:
        prime = x
        break

print('Prime: ' + str(prime))

