low_found = False
check_nums = [x for x in range(2, 21)]

num_check = 21
while not low_found:
    found = False
    for num in check_nums:
        if num_check % num != 0:
            found = True
            break
    if not found:
        low_found = True
        print(num_check)
    else:
        num_check += 1