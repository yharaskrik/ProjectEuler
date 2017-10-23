palindromes = []

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        if str(x * y) == str(x * y)[::-1]:
            if palindromes and x * y < max(palindromes):
                break
            palindromes.append(x * y)

print(str(max(palindromes)))