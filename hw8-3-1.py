# author: LM (AMDG) 12/8/21
def count_odds(lst):
    x = 0
    total = 0
    while x < len(lst):
        if lst[x] % 2 != 0:
            total += 1
        x += 1
   
    return total

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)
