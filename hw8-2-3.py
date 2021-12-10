# author: LM (AMDG) 12/9/2
def count_evens(lst): 
    total = 0
    x = 0
    while x < len(lst):
        if lst[x] % 2 != 0:
           total += 0
           break
    else:
        if lst[x] % 2 == 0:
            total += x
            x += 1
    return total 

print(count_evens([2, 4, 6, 8, 9]) == 20)
print(count_evens([13, 12, 10]) == 0)
print(count_evens([14, 16, 32]) == 62)
