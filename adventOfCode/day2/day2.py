file = open("day2/input.txt",'r')

how_many_safe = 0

for line in file:
    isSafe = True
    asc = False
    desc = False
    errors = 0
    unsafe = 0

    tab = [int(x) for x in line.split(' ')]
    for i in range(len(tab) - 1):
        if asc and desc:
            #print("TEST")
            isSafe = False
            errors += 1
        elif abs(tab[i] - tab[i+1]) > 3 or abs(tab[i] - tab[i+1]) == 0:
            #print(f"{tab[i]} : {tab[i+1]}")
            isSafe = False
            errors+=1

        if (tab[i] - tab[i + 1]) > 0:
            asc = True

        if (tab[i] - tab[i+1]) < 0:
            desc = True
    
    if desc and asc: 
        isSafe = False

    if isSafe or errors <= 1:
        print(tab)
        how_many_safe+=1

print(how_many_safe)